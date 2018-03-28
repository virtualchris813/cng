from pgdb import connect
from cng_db import dbhost, dbport, dbuser, dbpass, dbname

def verifyInput():
    if not dbname:
        print("You must define a database name (dbname) in cng_db.py. EXITING!")
        exit(1)
    if not dbpass:
        print("You must define a database password (dbpass) in cng_db.py. EXITING!")
        exit(1)
    if not dbuser:
        print("You must define a database user (dbuser) in cng_db.py. EXITING!")
        exit(1)
    if not dbport:
        print("You must define a database port (dbport) in cng_db.py. EXITING!")
        exit(1)
    if not dbhost:
        print("You must define a database host (dbhost) in cng_db.py. EXITING!")
        exit(1)

def checkIfBaseName(thisName):
    # See if there are any hostnames in the DB that match our base name
    # All names are stored in lowercase
    cursor.execute("select * from hostname where basename like (%s) order by incrementor desc limit 1", (thisName,))
    hQuery = cursor.fetchone()
    print(hQuery)
    return hQuery

def getLastIncrementor(thisName, thisIncSize):
    # Get the last incrementor from the current list of matching entries in the DB
    print("this name and size ", thisName, thisIncSize)
    cursor.execute("select incrementor from hostname where basename like (%s) and inc_width = (%d) order by id desc limit 1", (thisName, thisIncSize))
    hQuery = cursor.fetchone()
    if hQuery:
        hResult = hQuery.incrementor
        print("Hresult is ", hResult)
        return hResult

def makeName(base, incWidth):
    global nextInc
    lowerBase = base.lower()
    baseName = checkIfBaseName(lowerBase)
    # If the basename has been used, get the next incrementor
    # Otherwise, create a new one
    # When figured out, return the full name
    if baseName:
        thisInc = getLastIncrementor(lowerBase, incWidth)
#        print("thisInc is ", thisInc)
        if thisInc:
            nextInc = int(thisInc) + 1
#           print("nextInc is ", nextInc)
            newName = lowerBase + str(nextInc).zfill(incWidth)
#           print("New Name is ", newName)
        else:
            nextInc = 1
            newName = lowerBase + str(nextInc).zfill(incWidth)
#           print("Newname is ", newName)
    else:
        nextInc = 1
        newName = lowerBase + str(nextInc).zfill(incWidth)
    return newName

def insertName(baseName, inc, incWidth, fullName):
    # Add a name to the DB
    lBaseName = baseName.lower()
#    print("Inserting " + lBaseName + " " + str(inc) + " " + str(incWidth) + " " + fullName)
    cursor.execute("insert into hostname (basename, incrementor, inc_width, fullname) values (%s, %d, %d, %s)", (lBaseName, inc, incWidth, fullName))
    con.commit()

def queryName(fullName):
    fullNameLower = fullName.lower()
    print("Querying for name: ", fullNameLower)
    cursor.execute("select fullname from hostname where fullname like (%s)", (fullNameLower,))
    hQuery = cursor.fetchone()
    if hQuery:
        print("Found a result: ", hQuery.fullname)
        return True
    else:
        print("Did not find a match: ", fullNameLower)
        return False

def deleteName(fullName):
    fullNameLower = fullName.lower()
    print("Making sure a record exists to delete")
    isExist = queryName(fullName)
    if isExist:
        print("Deleting record for name: ", fullNameLower)
        cursor.execute("delete from hostname where fullname like (%s)", (fullNameLower,))
        con.commit()
        return True
    else:
        print("No record was found to delete")
        return False

def dbClose():
    cursor.close()
    con.close()

def newIncrementor():
    newInc = nextInc
    return nextInc

verifyInput()
con = connect(database=dbname, host=dbhost, port=int(dbport), user=dbuser, password=dbpass)
cursor = con.cursor()
