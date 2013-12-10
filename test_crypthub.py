import unittest
import os

import random

import crypthub

class CryptHubTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_entry_points(self):
        crypthub
        crypthub.github

    def test_getkeys(self):
        public_keys = crypthub.github.get_keys('rgbkrk')
        key_id = random.choice(public_keys.keys())

        assert 'ssh-rsa' in public_keys[key_id]

if __name__ == '__main__':
    unittest.main()
