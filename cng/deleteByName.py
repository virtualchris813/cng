from dbOps import deleteName, dbClose
inName = "labvmweb-000007"

def deleteByName(inName):
    deleted = deleteName(inName)
    return deleted
