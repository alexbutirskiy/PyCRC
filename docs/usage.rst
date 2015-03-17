========
Usage
========

To use PyCRC in a project, import the needed module::

    from PyCRC.CRC16 import CRC16
    from PyCRC.CRC16DNP import CRC16DNP
    from PyCRC.CRC16Kermit import CRC16Kermit
    from PyCRC.CRC16SICK import CRC16SICK
    from PyCRC.CRC32 import CRC32
    from PyCRC.CRCCCITT import CRCCCITT

Then, easy to use as::

    input = '12345'
    print(CRCCCITT().calculate(input))
    
or for hexa strings::

    input = b'\x05d\x05\xc0\x00\x01\x00\x0c'
    print(CRCCCITT().calculate(input))