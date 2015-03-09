# -*- coding: utf8 -*-

#
# CRC16SICK MODULE
#

from ctypes import c_ushort


class CRC16SICK(object):
    # The CRC's are computed using polynomials.
    # Here is the most used coefficient for CRC16 SICK
    crc16SICK_constant = 0x8005

    def __init__(self):
        pass

    def calculate(self, input_data=None):
        try:
            is_string = isinstance(input_data, str)
            is_bytes = isinstance(input_data, bytes)

            if not is_string and not is_bytes:
                raise Exception("Please provide a string or a byte sequence \
                    as argument for calculation.")

            crcValue = 0x0000

            for idx, c in enumerate(input_data):
                d = ord(c) if is_string else c
                short_c = 0x00ff & d

                idx_previous = idx - 1
                if idx_previous == -1:
                    prev_c = 0
                else:
                    prev_c = input_data[idx_previous]
                    prev_c = ord(prev_c) if is_string else prev_c

                short_p = (0x00ff & prev_c) << 8

                if (crcValue & 0x8000):
                    crcValue = c_ushort(
                        crcValue << 1).value ^ self.crc16SICK_constant
                else:
                    crcValue = c_ushort(crcValue << 1).value

                crcValue &= 0xffff
                crcValue ^= (short_c | short_p)

            # After processing, the one's complement of the CRC is calculated 
            # and the two bytes of the CRC are swapped.
            low_byte = (crcValue & 0xff00) >> 8
            high_byte = (crcValue & 0x00ff) << 8
            crcValue = low_byte | high_byte

            return crcValue
        except Exception as e:
            print("EXCEPTION(calculate): {}".format(e))
