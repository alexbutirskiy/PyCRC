#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST CRC16Kermit Module
"""

import unittest

from PyCRC.CRC16Kermit import CRC16Kermit  # NOQA


class CRC16KermitTest(unittest.TestCase):
    def setUp(self):
        self.crc = CRC16Kermit()

    def testNoneArgCalculate(self):
        msg = ("Providing calculate method with argument set to None should "
               "result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(None), msg)

    def testNoArgCalculate(self):
        msg = "Providing calculate method with no argument should return None"
        self.assertEqual(self.crc.calculate(), None, msg)

    def testCalculate(self):
        msg = "Calculated CRC16Kermit for 0123456789 should be 0x6E5F"
        self.assertEqual(
            self.crc.calculate("0123456789"), int('0x6E5F', 0), msg)

    def testTableItem42(self):
        msg = "The precalculated table's item #42 should be 0x8e58"
        self.assertEqual(self.crc.crc16kermit_tab[42], '0x8e58', msg)
 
    def testTableItem10(self):
        msg = "The precalculated table's item #10 should be 0xaf5a"
        self.assertEqual(self.crc.crc16kermit_tab[10], '0xaf5a', msg)

    def testTableItems(self):
        msg = ("After creating a CRC16Kermit object we must have a "
               "precalculated table with 256 items")
        self.assertEqual(len(self.crc.crc16kermit_tab), 256, msg)

    def testTableNotEmpty(self):
        msg = ("After creating a CRC16Kermit object we must have a "
               "precalculated table not empty")
        self.assertIsNot(self.crc.crc16kermit_tab, [], msg)


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
