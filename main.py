from edltools.core import Edl
from edltools.helpers import importEdlTitle, importEdlFcm, importEdlBody

path = "./Test EDLS/Avid/Avid Test EDL - Simple.edl"
path2 = "./Test EDLS/Resolve/Resolve Test EDL - Simple.edl"
path3 = "./Test EDLS/Avid/Avid Test EDL - Simple_WITH_Source.edl"

# print(importEdlBody(path))

testEDL = Edl(path3)


#print(testEDL)
# print(testEDL.__str__())
# print(testEDL.body)
print(testEDL.listFiles())

# Produce a software that compares any number of EDLs and checks for overlapping
# Compare source file lists?

# Build in some kind of archive price feature?
