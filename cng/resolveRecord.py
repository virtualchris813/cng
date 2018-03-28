##!env/bin/python
# Check if DNS record exists for a given name

import dns.resolver

def checkNameExists(lhName):
    try:
        dns.resolver.query(lhName)
        print "Record already exists for: " + lhName
        return True
    except(dns.exception.Timeout):
        print "Timed out querying the DNS server for " + lhName
        return True
    except:
        print "Record not found for: " + lhName
        print "Continuing..."
        return False
