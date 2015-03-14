# -*- coding: utf8 -*-

#
# CRC16DNP MODULE
#


from ctypes import c_ushort


class CRC16DNP(object):
    crc16dnp_tab = []

    # The CRC's are computed using polynomials.
    # Here is the most used coefficient for CRC16 DNP
    crc16dnp_constant = 0xA6BC

    def __init__(self):
        # initialize the precalculated tables
        if not len(self.crc16dnp_tab):
            self.init_crc16dnp()

    def calculate(self, input_data=None):
        try:
            is_string = isinstance(input_data, str)
            is_bytes = isinstance(input_data, bytes)

            if not is_string and not is_bytes:
                raise Exception("Please provide a string or a byte sequence "
                                "as argument for calculation.")

            crcValue = 0x0000

            for c in input_data:
                d = ord(c) if is_string else c
                tmp = crcValue ^ d
                rotated = (crcValue >> 8)
                crcValue = rotated ^ int(self.crc16dnp_tab[(tmp & 0x00ff)], 0)

            # after processing the one's complement of the CRC is calculated
            # and the two bytes of the CRC are swapped.
            crcValue ^= 0xffffffff  # (or crcValue = ~crcValue)
            low_byte = (crcValue & 0xff00) >> 8
            high_byte = (crcValue & 0x00ff) << 8
            crcValue = low_byte | high_byte

            return crcValue
        except Exception as e:
            print("EXCEPTION(calculate): {}".format(e))

    def init_crc16dnp(self):
        '''The algorithm use tables with precalculated values'''
        for i in range(0, 256):
            crc = c_ushort(i).value
            for j in range(0, 8):
                if (crc & 0x0001):
                    crc = c_ushort(crc >> 1).value ^ self.crc16dnp_constant
                else:
                    crc = c_ushort(crc >> 1).value
            self.crc16dnp_tab.append(hex(crc))
