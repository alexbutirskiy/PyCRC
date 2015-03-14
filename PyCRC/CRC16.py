# -*- coding: utf8 -*-

#
# CRC16 MODULE
#
# includes CRC16 and CRC16 MODBUS
#

from ctypes import c_ushort


class CRC16(object):
    crc16_tab = []

    # The CRC's are computed using polynomials. Here is the most used
    # coefficient for CRC16
    crc16_constant = 0xA001  # 40961

    def __init__(self, modbus_flag=False):
        # initialize the precalculated tables
        if not len(self.crc16_tab):
            self.init_crc16()
        self.mdflag = bool(modbus_flag)

    def calculate(self, input_data=None):
        try:
            is_string = isinstance(input_data, str)
            is_bytes = isinstance(input_data, bytes)

            if not is_string and not is_bytes:
                raise Exception("Please provide a string or a byte sequence "
                                "as argument for calculation.")

            crcValue = 0x0000 if not self.mdflag else 0xffff

            for c in input_data:
                d = ord(c) if is_string else c
                tmp = crcValue ^ d
                rotated = c_ushort(crcValue >> 8).value
                crcValue = rotated ^ int(self.crc16_tab[(tmp & 0x00ff)], 0)

            return crcValue
        except Exception as e:
            print("EXCEPTION(calculate): {}".format(e))

    def init_crc16(self):
        '''The algorithm uses tables with precalculated values'''
        for i in range(0, 256):
            crc = c_ushort(i).value
            for j in range(0, 8):
                if (crc & 0x0001):
                    crc = c_ushort(crc >> 1).value ^ self.crc16_constant
                else:
                    crc = c_ushort(crc >> 1).value
            self.crc16_tab.append(hex(crc))
