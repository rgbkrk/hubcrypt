import unittest
import os
import random
import json

import httpretty
import pytest

import hubcrypt

# Set up some "hokey" keys
key_dict = {
        6089446: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRkGTt3IW4snceuvep4scqRPx1IHPd7pRblLb611mcBb5Yo12jjp6vnyEhvxrSY85HVDXK4q7voeG1zTwAmeD7iJ2WeXi5a42UclVBcTxG1QePrFvv9NcZlNz39J9utfs8Hf+RPbMpa0FWw9+0Q9X8SPaQkmUQKnlBm29lYS7S/DWfowF0vu6jOaFJHECIgSA4WbudjVQyDTNvzcffdocMc1z5YaGSDuslK7OafZA1aDRWghU1vNUcP2ZN0h3JfGt56WauukJU19ZNuuIl25EgPuPTFLlq11Agp3p5cVpfo+Fym9ghCzzavxPKfeqGjrxq/dwBxH9MN85g3dSAM8b3",
        6272418: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYoqGyixCqMPldcF+L+3G9XVRDnEu6zgJP2UZuKlqrzsMkS7uSZZbS8PfV3KtfRyP23FzePNmHQR5/BDoxPYFVf4evppTMZVgGY4Pu+V+NtVh8YRNH5+2ZAR1kEelqF25y02Xnf69xEO1p/aovMoHP6/h8TBjpj2RNndE3efYtwSITvOFsBoZXDtuuFy1zUh7atDnfhEvkKRsR0NeOGcSHJSyMpGO33wnbhE/1ZjQW3iv+RwBM4YpLewOUCGenMUoFQl3589yGofP08FCToPocpEzXdF812zh39116moMTISlTkRuxcYI0X2NMgvREIypl1oW3Ziqs+V1M+BAPqUAx",
}

pem_of_pub = {
        6272418: """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KKhsosQqjD5XXBfi/tx
vV1UQ5xLus4CT9lGbipaq87DJEu7kmWW0vD31dyrX0cj9txc3jzZh0EefwQ6MT2B
VX+Hr6aUzGVYBmOD7vlfjbVYfGETR+ftmQEdZBHpahductNl53+vcRDtaf2qLzKB
z+v4fEwY6Y9kTZ3RN3n2LcEiE7zhbAaGVw7brhctc1Ie2rQ534RL5CkbEdDXjhnE
hyUsjKRjt98J24RP9WY0Ft4r/kcATOGKS3sDlAhnpzFKBUJd+fPchqHz9PBQk6D6
HKRM13RfNds4d/ddepqDEyEpU5EbsXGCNF9jTIL0RCMqZdaFt2YqrPldTPgQD6lA
MQIDAQAB
-----END PUBLIC KEY-----
""".strip(),
       6089446: """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0ZBk7dyFuLJ3Hrr3qeLH
KkT8dSBz3e6UW5S2+tdZnAW+WKNdo46er58hIb8a0mPOR1Q1yuKu76Hhtc08AJng
+4idlnl4uWuNlHJVQXE8RtUHj6xb7/TXGZTc9/SfbrX7PB3/kT2zKWtBVsPftEPV
/Ej2kJJlECp5QZtvZWEu0vw1n6MBdL7uozmhSRxAiIEgOFm7nY1UMg0zb83H33aH
DHNc+WGhkg7rJSuzmn2QNWg0VoIVNbzVHD9mTdIdyXxreelmrrpCVNfWTbriJduR
ID7j0xS5atdQIKd6eXFaX6PhcpvYIQs82r8Tyn3qho68av3cAcR/TDfOYN3UgDPG
9wIDAQAB
-----END PUBLIC KEY-----
""".strip()
}

github_api_response_python = [{"id":key_id, "key": key} for (key_id, key) in key_dict.items()]
github_api_response = json.dumps(github_api_response_python)

class HubcryptTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_entry_points(self):
        hubcrypt
        hubcrypt.github
        hubcrypt.github.GitHub
        hubcrypt.crypt

    @httpretty.activate
    def test_getkeys(self):
        httpretty.register_uri(httpretty.GET,
                               "https://api.github.com/users/rgbkrk/keys",
                               body=github_api_response,
                               content_type="application/json")

        gh = hubcrypt.github.GitHub()
        public_keys = gh.get_keys('rgbkrk')
        key_id = random.choice(public_keys.keys())

        assert key_dict[key_id] in public_keys[key_id]

    @httpretty.activate
    def test_getkey(self):
        httpretty.register_uri(httpretty.GET,
                               "https://api.github.com/users/rgbkrk/keys",
                               body=github_api_response,
                               content_type="application/json")
        gh = hubcrypt.github.GitHub()

        # Don't care whether it's a string or integer
        public_key = gh.get_key('rgbkrk', '6089446')
        assert public_key == key_dict[6089446]

        public_key = gh.get_key('rgbkrk', 6089446)
        assert public_key == key_dict[6089446]

        with pytest.raises(KeyError) as exc_info:
            public_key = gh.get_key('rgbkrk', 1)

        key_error = exc_info.value
        assert "Key with ID 1 does not exist for user rgbkrk" == key_error.message

    @httpretty.activate
    def test_setting_endpoint(self):
        httpretty.register_uri(httpretty.GET,
                               "https://github.crypthub.com/api/v3/users/rgbkrk/keys",
                               body=github_api_response,
                               content_type="application/json")

        gh = hubcrypt.github.GitHub(endpoint='https://github.crypthub.com/api/v3')

        # Don't care whether it's a string or integer
        public_key = gh.get_key('rgbkrk', '6089446')
        assert public_key == key_dict[6089446]

        public_key = gh.get_key('rgbkrk', 6089446)
        assert public_key == key_dict[6089446]

    def test_convert_key(self):
        # Test each of our sample keys
        for key_id in key_dict:
            pem_key = hubcrypt.crypt.convert_key(key_dict[key_id])
            assert pem_key == pem_of_pub[key_id]

if __name__ == '__main__':
    unittest.main()
