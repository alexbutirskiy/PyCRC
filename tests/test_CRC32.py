#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST CRC32 Module
"""

import unittest

from PyCRC.CRC32 import CRC32  # NOQA


class CRC32Test(unittest.TestCase):
    def setUp(self):
        self.crc = CRC32()

    def testNoneArgCalculate(self):
        msg = ("Providing calculate method with argument set to None should "
               "result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(None), msg)

    def testNoArgCalculate(self):
        msg = ("Providing calculate method with no argument should "
               "result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(None), msg)

    def testCalculate(self):
        msg = "Calculated CRC32 for 0123456789 should be 0xA684C7C6"
        self.assertEqual(
            self.crc.calculate("0123456789"), int('0xA684C7C6', 0), msg)

    def testTableItem42(self):
        msg = "The precalculated table's item #42 should be 0xdbbbc9d6"
        self.assertEqual(self.crc.crc32_tab[42], '0xdbbbc9d6', msg)

    def testTableItem10(self):
        msg = "The precalculated table's item #10 should be 0xe0d5e91e"
        self.assertEqual(self.crc.crc32_tab[10], '0xe0d5e91e', msg)

    def testTableItems(self):
        msg = ("After creating a CRC32 object we must have a precalculated "
               "table with 256 items")
        self.assertEqual(len(self.crc.crc32_tab), 256, msg)

    def testTableNotEmpty(self):
        msg = ("After creating a CRC32 object we must have "
               "a precalculated table not empty")
        self.assertIsNot(self.crc.crc32_tab, [], msg)


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
