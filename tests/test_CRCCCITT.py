#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST CRCCCITT Module
"""

import unittest

from PyCRC.CRCCCITT import CRCCCITT  # NOQA


class CRCCCITTTest(unittest.TestCase):

    def setUp(self):
        self.crc_1 = CRCCCITT(version='XModem')
        self.crc_2 = CRCCCITT(version='FFFF')
        self.crc_3 = CRCCCITT(version='1D0F')

    def testNoVersionInit(self):
        msg = ("Providing no version at initialization should result "
               "in an Exception")
        self.assertRaises(Exception, CRCCCITT(version=None), msg)

    def testWrongVersionInit(self):
        msg = ("Providing wrong version at initialization should result "
               "in an Exception")
        self.assertRaises(Exception, CRCCCITT(version='WrongVersion'), msg)

    def testNoneArgCalculate(self):
        msg = ("Providing calculate method with argument set to None should "
               "result in an Exception")
        self.assertRaises(Exception, self.crc_1.calculate(None), msg)

    def testNoArgCalculate(self):
        msg = ("Providing calculate method with no argument should return "
               "result in an Exception")
        self.assertRaises(Exception, self.crc_1.calculate(), msg)

    def testCalculateVersion3(self):
        msg = "Calculated CRC CCITT (0x1D0F) for 0123456789 should be 0x18A1"
        self.assertEqual(
            self.crc_3.calculate("0123456789"), int('0x18A1', 0), msg)

    def testCalculateVersion2(self):
        msg = "Calculated CRC CCITT (0xFFFF) for 0123456789 should be 0x7D61"
        self.assertEqual(
            self.crc_2.calculate("0123456789"), int('0x7D61', 0), msg)

    def testCalculateVersion1(self):
        msg = "Calculated CRC CCITT (XModem) for 0123456789 should be 0x9C58"
        self.assertEqual(
            self.crc_1.calculate("0123456789"), int('0x9C58', 0), msg)

    def testTableItem42(self):
        msg = "The precalculated table's item #42 should be 0x8528"
        self.assertEqual(self.crc_1.crc_ccitt_tab[42], '0x8528', msg)

    def testTableItem10(self):
        msg = "The precalculated table's item #10 should be 0xa14a"
        self.assertEqual(self.crc_1.crc_ccitt_tab[10], '0xa14a', msg)

    def testTableItems(self):
        msg = ("After creating a CRC CCITT object we must have a "
               "precalculated table with 256 items")
        self.assertEqual(len(self.crc_1.crc_ccitt_tab), 256, msg)

    def testTableNotEmpty(self):
        msg = ("After creating a CRC CCITT object we must have a "
               "precalculated table not empty")
        self.assertIsNot(self.crc_1.crc_ccitt_tab, [], msg)


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
