from cng_vars import hNameFormat, hIncLength
from dbOps import makeName, insertName, dbClose, newIncrementor
from resolveRecord import checkNameExists

dash = "-"
underscore = "_"
errorMessage = ""

def getIncrementor(num):
    if num > 0:
        global nameIncrementor
        nameIncrementor = num + 1
    return nameIncrementor

def getIncrementorSize():
    incLength = str(hIncLength)
    return incLength

def generateName(hFields):
    global hNameWoInc
    hNameWoInc = ""
    hNameFields = hNameFormat()
    formatFields = hNameFields.split(" ")
    for i in formatFields:
        if i == "dash":
            hNameWoInc = hNameWoInc + dash
        elif i == "underscore":
            hNameWoInc = hNameWoInc + underscore
        elif i == "hLoc":
            hLoc = hFields[i]
            hNameWoInc = hNameWoInc + hLoc
        elif i == "hType":
            hType = hFields[i]
            hNameWoInc = hNameWoInc + hType
        elif i == "hApp":
            hApp = hFields[i]
            hNameWoInc = hNameWoInc + hApp
        elif i == "hUser1":
             hUser1 = hFields[i]
             hNameWoInc = hNameWoInc + hUser1
        elif i == "hUser2":
            hUser2 = hFields[i]
            hNameWoInc = hNameWoInc + hUser2
        elif i == "hUser3":
            hUser3 = hFields[i]
            hNameWoInc = hNameWoInc + hUser3
        elif i == "hUser4":
            hUser4 = hFields[i]
            hNameWoInc = hNameWoInc + hUser4
        elif i == "hUser5":
            hUser5 = hFields[i]
            hNameWoInc = hNameWoInc + hUser5
        else:
            print("Expected " + hNameFields.len() + "fields but didnt get the right number. \n")
            print("Plese check your input fields as well as fieldOrder in cng_vars.py")
            exit(1)
    global hIncSize
    hIncSize = getIncrementorSize()
    hInc = getIncrementor(int(hIncSize))
    hName = makeName(hNameWoInc, hInc)
    return (hName)

def addName(baseName, inc, incWidth, fullName):
    print("Basename is ", baseName)
    print("inc is", inc)
    print("incWidth is ", incWidth)
    print("fullName is ", fullName)
    if checkNameExists(fullName):
        print("Name is already found, exiting.")
        global isError 
        isError = 1
        errorMessage = "Error checking DNS name for " + fullName
    else:
        print("Name not found, creating in DB")
        global isError
        isError = 0
    	insertName(baseName, inc, incWidth, fullName)

def addNewName(hFields):
    hName = generateName(hFields)
    newInc=newIncrementor()
    addName(hNameWoInc, newInc, nameIncrementor, hName)
    print(isError)
    if isError == 0:
        return(hName)
    else:
        errorMessage = "Error - Failed due to problem with inputs. Please check your fields"
        return(errorMessage)
