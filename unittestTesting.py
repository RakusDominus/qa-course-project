import requests
import Konstante
import unittest

class TestSajt(unittest.TestCase):

    def test_RadiLiSajt(self):
        response= requests.get(Konstante.BASE_URL,timeout=10)
        assert response.status_code==200

    def test_Login(self):
        response= requests.post(Konstante.BASE_URL + Konstante.LOGIN_API,{
            "email":"sapna2661@gmail.com",
            "password":"Sap937rattu"
        })
        assert response.status_code==200


if __name__ == '__main__':
    unittest.main()


