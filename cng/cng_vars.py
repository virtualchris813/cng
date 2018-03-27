# This file defines the format of your hostnames
# Hostnames can be created in any way you'd like
# as long as they follow the format defined in this
# file. Examples are provided to assist in the formatting.

# A hostname is made up of several components.
# At a minimum you will need one component and
# an incrementor defined. Its best to have several
# components so the names are somewhat unique but
# do as you wish.

# The fields available to build a custom hostname are listed below:
#dash       =  A literal dash, "-"
#underscore =  An underscore, "_"
#hLoc       =  A location code, for example FL (Florida)
#hType      =  A system type, for example VM
#hApp       =  An application type, for example APP
#hUser1     =  A user defined string, whatever you want to fit your naming standard
#hUser2     =  A user defined string, whatever you want to fit your naming standard
#hUser3     =  A user defined string, whatever you want to fit your naming standard
#hUser4     =  A user defined string, whatever you want to fit your naming standard
#hUser5     =  A user defined string, whatever you want to fit your naming standard
#hIncLength =  The size of the incrementor, for eaxample 3 would result in the 1st being 001

# EXAMPLES
# To create hostnames with a format of:
# APP TYPE 6 digit incrementor
# For example the 23rd web server VM:
# WEBVM000023
# You would define fieldOrder as:
# fieldOrder = "hApp hType"
# and you would define hIncLength as:
# hIncLength = 6

# To create hostnames with a format of:
# LOCATION TYPE APP DATACENTER DASH 4 digit incrementor
# For example the 5th VM in Florida running an app server in data center 1:
# FLVMAPPDC1-0005
# You would define fieldOrder as:
# fieldOrder = "hLoc hType hApp hUser1 dash"
# and you would define hIncLength as:
# hIncLength = 4

# To create hostnames with a format of:
# ORGINIZATION UNDERSCORE LOCATION UNDERSCORE APP TYPE DASH PROJECT CODE DASH 2 digit incrementor
# For example the 2nd web server VM owned by finance in Atlanta on project pg4:
# FIN_ATL_WEBVM-pg4-02
# You would define fieldOrder as:
# fieldOrder = "hUser1 underscore hLoc underscore hApp hType dash hUser2 dash"
# and you would define hIncLength as:
# hIncLength = 2

# Please define your desired format in the fieldOrder definition below:
def hNameFormat():
    fieldOrder = "F_ORDER"
    # fieldOrder = "hUser1 underscore hLoc underscore hApp hType dash hUser2 dash"
    return fieldOrder

hNameFormat()
hIncLength = I_LEN
