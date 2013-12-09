import unittest
import os

import random

import hubcrypt

class HubcryptTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_entry_points(self):
        hubcrypt
        hubcrypt.github

    def test_getkeys(self):
        public_keys = hubcrypt.github.get_keys('rgbkrk')
        key_id = random.choice(public_keys.keys())

        assert 'ssh-rsa' in public_keys[key_id]

if __name__ == '__main__':
    unittest.main()
