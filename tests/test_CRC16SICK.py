#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST CRC16SICK Module
"""

import unittest

from PyCRC.CRC16SICK import CRC16SICK  # NOQA


class CRC16SICKTest(unittest.TestCase):
    def setUp(self):
        self.crc = CRC16SICK()

    def testNoneArgCalculate(self):
        msg = ("Providing calculate method with argument set to None should "
               "result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(None), msg)

    def testNoArgCalculate(self):
        msg = ("Providing calculate method with no argument should result"
               " in an Exception")
        self.assertRaises(Exception, self.crc.calculate(), msg)

    def testCalculate(self):
        msg = "Calculated CRC16SICK for 0123456789 should be 0xF6C6"
        self.assertEqual(
            self.crc.calculate("0123456789"), int('0xF6C6', 0), msg)


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
