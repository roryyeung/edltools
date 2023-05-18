from edltools.core import Edl
from edltools.helpers import importEdlTitle, importEdlBody

testEdl = "./tests/TTN_Shark with Steve Backshall_Ep1_Atlantic_Ocean_NBCU_MASTER.edl"

print(importEdlTitle(testEdl))
print(importEdlBody(testEdl))