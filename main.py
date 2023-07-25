from edltools.core import Edl, edlDupeDetection
from edltools.helpers import importEdlTitle, importEdlFcm, importEdlBody, exportXls

#path = "./Test EDLS/Avid/Avid Test EDL - Simple.edl"
#path2 = "./Test EDLS/Resolve/Resolve Test EDL - Simple.edl"
#path3 = "./Test EDLS/Avid/Avid Test EDL - Simple_WITH_Source.edl"

# print(importEdlBody(path))

# testEDL = Edl(path3)


# print(testEDL)
# print(testEDL.__str__())
# print(testEDL.body)
# print(testEDL.listFiles())

# Produce a software that compares any number of EDLs and checks for overlapping
# Compare source file lists?

# Build in some kind of archive price feature?

#path = "./Test Exports/"
#fileName = "Hello World.xlsx"
#joinedPath = os.path.join(path,fileName)

#exportXls(testEDL.body,joinedPath)

projectPath = "TTN_Working/230724_TTN_Whale with Steve Backshall_Ep3_Ocean Voyagers_PL_50m17s.edl"
sourcePath1 = "TTN_Working/230612_TTN_Whale with Steve Backshall_Ep1_Whales and Us_PL_EOE_50m29s21f.edl"
sourcePath2 = "TTN_Working/230714_TTN_Whale with Steve Backshall_Ep2_Ocean Hunters_PL_EOE_50m02s03f.edl"

projectEdl = Edl(projectPath)
sourceEdl = [Edl(sourcePath1),Edl(sourcePath2)]
reused = edlDupeDetection(projectEdl,sourceEdl)
print(set(reused))