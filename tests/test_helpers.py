import sys
sys.path.insert(0, '../edltools')
from unittest import TestCase
from edltools.helpers import importEdlTitle


class IngestHelpersTest(TestCase):
    def test_helpers(self):
        filepath = "./tests/TTN_Shark with Steve Backshall_Ep1_Atlantic_Ocean_NBCU_MASTER.edl"
        title = importEdlTitle(filepath)
        expected = "TTN_Shark with Steve Backshall_Ep1_Atlantic_Ocean_NBCU_MASTER"
        assert title == expected