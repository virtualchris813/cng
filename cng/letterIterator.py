# Allows us to add a letter based iterator to a name
# for example using a A,B,C...X,Y,Z->ZZ
# This is for a specific usecase but could be easily modified
# to allow a greater (or smaller) range.

currIter =
chr(ord('a') + 5)