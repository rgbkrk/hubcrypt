#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class GitHub(object):
    def __init__(self, endpoint="https://api.github.com"):
        self.endpoint = endpoint.rstrip("/")

    def get_keys(self, username):
        '''Get the public keys of user named `username` from GitHub. Returns a
        dictonary mapping the id (from GitHub) to the public key.

        >>> gh = GitHub()
        >>> gh.get_keys('rgbkrk') # doctest: +ELLIPSIS
        ...                    # doctest: +NORMALIZE_WHITESPACE
        {6089446: u'ssh-rsa AAAA...',
         6272418: u'ssh-rsa AAAA...'}
        '''

        keys_url = self.endpoint + "/users/{}/keys".format(username)
        resp = requests.get(keys_url)
        resp.raise_for_status()

        keys = resp.json()

        return {idkey['id']: idkey['key'] for idkey in keys}

    def get_key(self, username, key_id):
        '''
        Return the key specified by key_id

        >>> gh = GitHub()
        >>> gh.get_key('rgbkrk', 6272418)
        '''
        keys = self.get_keys(username)

        if(key_id not in keys):
            raise KeyError("Key with ID {} does not exist ".format(key_id) +
                           "for user {}".format(username))

        return keys[key_id]

