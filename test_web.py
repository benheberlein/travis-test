import pytest
from flask import Flask, json
from application import *

class TestWeb:
    
    def test_home(self):

        # Test GET on root
        response = application.test_client().get("/")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)
        
        assert(b"BAD INPUT" not in response.data)
    
    def test_404(self):
        response = application.test_client().get("/badroute")
        assert(response.status_code == 404)   
 
    def test_bad_req(self):
    
        # Test non numerical input number
        response = application.test_client().post("/", 
                        data=b"text=NotANumber&base=16", 
                        content_type="application/x-www-form-urlencoded")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)
        
        assert(b"BAD INPUT" in response.data)

        # Test partially numeric input
        response = application.test_client().post("/", 
                        data=b"text=100abc&base=NotANumber", 
                        content_type="application/x-www-form-urlencoded")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)
        
        assert(b"BAD INPUT" in response.data)

       # Test negative numeric input
        response = application.test_client().post("/", 
                        data=b"text=-200abc&base=2", 
                        content_type="application/x-www-form-urlencoded")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)
        
        assert(b"BAD INPUT" in response.data)

        # Test non numerical base
        response = application.test_client().post("/", 
                        data=b"text=100&base=NotANumber", 
                        content_type="application/x-www-form-urlencoded")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)
        
        assert(b"BAD INPUT" in response.data)
       
        # Test out of range base
        response = application.test_client().post("/", 
                        data=b"text=100&base=0", 
                        content_type="application/x-www-form-urlencoded")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)
        
        assert(b"BAD INPUT" in response.data)


    def test_good_req(self):
        
        # Test all bases
        for i in range(2, 16):
            response = application.test_client().post("/", 
                        data=str.encode("text=100&base=" + str(i)),
                        content_type="application/x-www-form-urlencoded")
            assert(response.status_code == 200)
            assert(b"Decimal to Arbitrary Base Converter" in response.data)
            assert(b"Enter a number" in response.data)
            assert(b"Enter a base" in response.data)
            assert(b"DevOps in the Cloud" in response.data)
        
            assert(str.encode(convert_wrap(100, i)) in response.data)

        # Test one long one      
        response = application.test_client().post("/", 
                        data=str.encode("text=12345678901234567890&base=16"),
                        content_type="application/x-www-form-urlencoded")
        assert(response.status_code == 200)
        assert(b"Decimal to Arbitrary Base Converter" in response.data)
        assert(b"Enter a number" in response.data)
        assert(b"Enter a base" in response.data)
        assert(b"DevOps in the Cloud" in response.data)

        assert(b"0x AB54A98CEB1F0AD2" in response.data)









