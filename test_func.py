import pytest
from flask import Flask
from application import *

class TestFunc:
    
    def test_convert(self):
        for i in range(2,16):
            assert (convert(0, i) == "0")
            assert (convert(1, i) == "1")
        
        assert(convert(100, 2) == "1100100")
        assert(convert(100, 3) == "10201")
        assert(convert(100, 4) == "1210")
        assert(convert(100, 5) == "400")
        assert(convert(100, 6) == "244")
        assert(convert(100, 7) == "202")
        assert(convert(100, 8) == "144")
        assert(convert(100, 9) == "121")
        assert(convert(100, 10) == "100")
        assert(convert(100, 11) == "91")
        assert(convert(100, 12) == "84")
        assert(convert(100, 13) == "79")
        assert(convert(100, 14) == "72")
        assert(convert(100, 15) == "6A")
        assert(convert(100, 16) == "64")
        
        assert(convert(1234567890123, 2) == "10001111101110001111110110000010011001011")
        assert(convert(1234567890123, 16) == "11F71FB04CB")
        

    def test_verify(self):
        assert(verify("1") == True)
        assert(verify("100") == True)
        assert(verify("1234567890123") == True)
        assert(verify("-100") == False)
        assert(verify("-10000000000") == False)
        assert(verify("0") == True)
        assert(verify("123abc") == False)
        assert(verify("AFE") == False)
        assert(verify("0000001") == True)

    def test_verify_base(self):
        assert(verify_base("0") == False)
        assert(verify_base("1") == False)
        for i in range(2, 16):
            assert(verify_base(str(i)) == True)
        assert(verify_base("17") == False)
        assert(verify_base("abc") == False)
        assert(verify_base("abc123") == False)
        assert(verify_base("-10") == False)

    def test_to_int(self):
        assert(to_int("123") == 123)
        assert(to_int("1") == 1)
        assert(to_int("-10") == -10)

    def test_convert_wrap(self):
        assert(convert_wrap(100, 2) == "0b 1100100")
        assert(convert_wrap(100, 3) == "0t 10201")
        assert(convert_wrap(100, 4) == "0q 1210")
        assert(convert_wrap(100, 5) == "0p 400")
        assert(convert_wrap(100, 6) == "0s 244")
        assert(convert_wrap(100, 7) == "0h 202")
        assert(convert_wrap(100, 8) == "0o 144")
        assert(convert_wrap(100, 9) == "0n 121")
        assert(convert_wrap(100, 10) == "0d 100")
        assert(convert_wrap(100, 11) == "0u 91")
        assert(convert_wrap(100, 12) == "0v 84")
        assert(convert_wrap(100, 13) == "0w 79")
        assert(convert_wrap(100, 14) == "0y 72")
        assert(convert_wrap(100, 15) == "0z 6A")
        assert(convert_wrap(100, 16) == "0x 64")
        
        assert(convert_wrap(1234567890123, 2) == "0b 10001111101110001111110110000010011001011")
        assert(convert_wrap(1234567890123, 16) == "0x 11F71FB04CB")
