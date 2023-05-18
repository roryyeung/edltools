from edltools.core import Edl
from edltools.helpers import importEdlTitle, importEdlBody

path = "./tests/TTN_Shark with Steve Backshall_Ep3_Pacific_Ocean_NBCU_MASTER_WITH_Source.edl"

#print(importEdlTitle(path))
#print(importEdlBody(path))

testEDL = Edl(path)

#print(testEDL)
#print(testEDL.body)
print(testEDL.listFiles())

# Produce a software that compares any number of EDLs and checks for overlapping
# Compare source file lists?

# Build in some kind of archive price feature?

