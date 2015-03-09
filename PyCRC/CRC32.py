# -*- coding: utf8 -*-

#
# CRC32 MODULE
#

from ctypes import c_ulong


class CRC32(object):
    crc32_tab = []

    # The CRC's are computed using polynomials. Here is the most used
    # coefficient for CRC32
    crc32_constant = 0xEDB88320

    def __init__(self):
        # initialize the precalculated tables
        if not len(self.crc32_tab):
            self.init_crc32()

    def calculate(self, input_data=None):
        try:
            is_string = isinstance(input_data, str)
            is_bytes = isinstance(input_data, bytes)

            if not is_string and not is_bytes:
                raise Exception("Please provide a string or a byte sequence as \
                    argument for calculation.")

            crcValue = 0xffffffff

            for c in input_data:
                d = ord(c) if is_string else c
                tmp = crcValue ^ d
                crcValue = (crcValue >> 8) ^ int(
                    self.crc32_tab[(tmp & 0x00ff)], 0)

            # Only for CRC-32: When all bytes have been processed, take the
            # one's complement of the obtained CRC value
            crcValue ^= 0xffffffff  # (or crcValue = ~crcValue)

            return crcValue
        except Exception as e:
            print("EXCEPTION(calculate): {}".format(e))

    def init_crc32(self):
        '''The algorithm use tables with precalculated values'''
        for i in range(0, 256):
            crc = i
            for j in range(0, 8):
                if (crc & 0x00000001):
                    crc = int(c_ulong(crc >> 1).value) ^ self.crc32_constant
                else:
                    crc = int(c_ulong(crc >> 1).value)
            self.crc32_tab.append(hex(crc))
