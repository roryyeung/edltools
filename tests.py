import sys
sys.path.insert(0, '../edltools')
import os
import unittest
from edltools.core import Edl
from edltools.helpers import importEdlTitle, importEdlBody, importEdlFcm, exportXls
from openpyxl import load_workbook

class ImportEdlTests(unittest.TestCase):

    def test_import_simple_Avid_Edl(self):
        """Checks that it's able to generate an EDL object from an Avid File129 type EDL."""
        edlPath="./Test EDLS/Avid/Avid Test EDL - Simple.edl"
        edlObject = Edl(edlPath)
        expectedString = "EDL object - Title: TTN_Shark with Steve Backshall_Ep1_Atlantic_Ocean_NBCU_MASTER, Frame Rate: 25, Length: 11 lines."
        self.assertEqual(edlObject.__str__(),expectedString, "Error generating EDL Object from Avid")

    def test_import_simple_Resolve_Edl(self):
        """Checks that it's able to generate an EDL object from Davinchi Resolve."""
        edlPath="./Test EDLS/Resolve/Resolve Test EDL - Simple.edl"
        edlObject = Edl(edlPath)
        expectedString = "EDL object - Title: Timeline 1, Frame Rate: 25, Length: 2 lines."
        self.assertEqual(edlObject.__str__(),expectedString, "Error generating EDL Object from Resolve")

class EdlMethodsTests(unittest.TestCase):

    def test_EdlListFiles(self):
        """Checks that an EDL provides the expected list of source files"""
        edlPath = "./Test EDLS/Avid/Avid Test EDL - Simple_WITH_Source.edl"
        edlObject = Edl(edlPath)
        expectedList = ['AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB','AU603_SHARKS_WITH_STEVE_BACKSHALL_3_PACIFIC_178FF_TXM_UHD_EN-GB']
        self.assertEqual(edlObject.listFiles(),expectedList,"Error with listFiles method - not expected list of files")

    def test_EdlListFiles_Nonetype(self):
        """Checks that if an EDL provides no source files, that an error is raised"""
        edlPath="./Test EDLS/Avid/Avid Test EDL - Simple.edl"
        edlObject = Edl(edlPath)
        with self.assertRaises(ValueError): edlObject.listFiles()

class ALEMethodsTests(unittest.TestCase):
    
    def test_AleListFiles(self):
        pass
    
    def test_AleListFiles_Nonetype(self):
        pass

class HelpersTests(unittest.TestCase):
    
    def test_importEdlTitle(self):
        """Checks that the EDL has the expected Title property."""
        path = "./Test EDLS/Avid/Avid Test EDL - Simple.edl"
        expectedTitle = "TTN_Shark with Steve Backshall_Ep1_Atlantic_Ocean_NBCU_MASTER"
        title = importEdlTitle(path)
        self.assertEqual(title,expectedTitle, "Error reading title - error with helper function: importEdlTitle")

    def test_importEdlBody(self):
        """ Checks that the EDL has the expected body property."""
        path = "./Test EDLS/Avid/Avid Test EDL - Simple.edl"
        expectedBody = [{
                'clip': ['000001', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'V', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000002', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000003', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A2', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000004', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A3', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000005', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A4', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000006', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A5', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000007', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A6', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000008', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A7', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000009', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A8', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000010', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A9', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }, {
                'clip': ['000011', 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5', 'A10', 'C', '00:58:30:00', '01:46:39:11', '01:00:00:00', '01:48:09:11'],
                'FROM CLIP NAME': 'AU601_SHARKS_WITH_STEVE_BACKSHALL_1_ATLANTIC_178FF_TXM_UHD_EN-GB_V5.NEW.01'
            }]
        body = importEdlBody(path)
        self.assertEqual(body,expectedBody, "Error reading body - error with helper function: importEdlBody")

    def test_importEdlFcm(self):
        """Checks that the EDL has the expected drop frame inforation."""
        path = "./Test EDLS/Avid/Avid Test EDL - Simple.edl"
        expectedFcm = "NON-DROP FRAME"
        Fcm = importEdlFcm(path)
        self.assertEqual(Fcm,expectedFcm, "Error reading Fcm - error with helper function: importEdlFcm")
        
class XlsHelpersTests(unittest.TestCase):

    def test_savesExcel(self):
        """Checks that the helper method saves a generic body object to an xlsx file correctly."""
        testPath="./Test Exports/savesExcel.xlsx"
        # Cleans up any existing test files
        if os.path.exists("./Test Exports/savesExcel.xlsx"):
            os.remove("./Test Exports/savesExcel.xlsx")
        # Write test file
        body = [{'Key1':'Val1','Key2':'Val2'},{'Key1':'Val3','Key2':'Val4'}]
        exportXls(body,testPath)
        # Load and check test file
        workbook = load_workbook(filename = testPath)
        sheet = workbook.active
        self.assertEqual(sheet['B2'].value,"Val2")

if __name__ == '__main__':
    unittest.main()