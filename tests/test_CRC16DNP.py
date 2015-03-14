#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST CRC16DNP Module
"""

import unittest

from PyCRC.CRC16DNP import CRC16DNP  # NOQA


class CRC16DNPTest(unittest.TestCase):
    def setUp(self):
        self.crc = CRC16DNP()

    def testNoneArgCalculate(self):
        msg = ("Providing calculate method with argument set to None "
               "should result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(None), msg)

    def testNoArgCalculate(self):
        msg = "Providing calculate method with no argument should return None"
        self.assertEqual(self.crc.calculate(), None, msg)

    def testCalculate(self):
        msg = "Calculated CRC16DNP for 0123456789 should be 0x7267"
        self.assertEqual(
            self.crc.calculate("0123456789"), int('0x7267', 0), msg)

    def testTableItem42(self):
        msg = "The precalculated table's item #42 should be 0xba9a"
        self.assertEqual(self.crc.crc16dnp_tab[42], '0xba9a', msg)

    def testTableItem10(self):
        msg = "The precalculated table's item #10 should be 0x9335"
        self.assertEqual(self.crc.crc16dnp_tab[10], '0x9335', msg)

    def testTableItems(self):
        msg = ("After creating a CRC16DNP object we must have a precalculated "
               "table with 256 items")
        self.assertEqual(len(self.crc.crc16dnp_tab), 256, msg)

    def testTableNotEmpty(self):
        msg = ("After creating a CRC16DNP object we must have a precalculated"
               " table not empty")
        self.assertIsNot(self.crc.crc16dnp_tab, [], msg)


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
