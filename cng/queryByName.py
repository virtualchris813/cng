from dbOps import queryName, dbClose


def queryByName(inName):
    tOrF = queryName(inName)
    return tOrF
