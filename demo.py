#!/usr/bin/env python3
# -*- coding: utf8 -*-

#
# EXAMPLE USAGE FOR CRC Module
#
#

from PyCRC.CRC16 import CRC16
from PyCRC.CRC16DNP import CRC16DNP
from PyCRC.CRC16Kermit import CRC16Kermit
from PyCRC.CRC16SICK import CRC16SICK
from PyCRC.CRC32 import CRC32
from PyCRC.CRCCCITT import CRCCCITT

if __name__ == "__main__":
    # for hex strings use bytearray to transform to a bytes sequence
    # bytearray.fromhex('056405c00001000c') -> b'\x05d\x05\xc0\x00\x01\x00\x0c'

    # HEXADECIMAL EXAMPLE
    target = b'\x05d\x05\xc0\x00\x01\x00\x0c'

    # DECIMAL EXAMPLE
    # target = '12341234'

    print("The results for {} are".format(target))
    print("{:20s} {:10X}".format(
        'CRC-CCITT(XModem)', CRCCCITT().calculate(target)))
    print("{:20s} {:10x}".format(
        'CRC-CCITT(0xFFFF)', CRCCCITT(version="FFFF").calculate(target)))
    print("{:20s} {:10x}".format(
        'CRC-CCITT(0x1D0F)', CRCCCITT(version="1D0F").calculate(target)))
    print("{:10s} {:20X}".format('CRC-16', CRC16().calculate(target)))
    print("{:20s} {:10X}".format(
        'CRC-16 (Modbus)', CRC16(modbus_flag=True).calculate(target)))
    print("{:20s} {:10X}".format(
        'CRC-16 (SICK)', CRC16SICK().calculate(target)))
    print("{:20s} {:10X}".format('CRC-DNP', CRC16DNP().calculate(target)))
    print("{:20s} {:10X}".format('CRC-32', CRC32().calculate(target)))
    print("{:20s} {:10X}".format(
        'CRC-16 (Kermit)', CRC16Kermit().calculate(target)))
