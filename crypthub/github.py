#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_keys(username):
    '''Get the public keys of user named `username` from GitHub. Returns a
    dictonary mapping the id (from GitHub) to the public key.

    >>> get_keys('rgbkrk') # doctest: +ELLIPSIS
    ...                    # doctest: +NORMALIZE_WHITESPACE
    {6089446: u'ssh-rsa AAAA...',
     6272418: u'ssh-rsa AAAA...'}
    '''

    resp = requests.get("https://api.github.com/users/rgbkrk/keys")
    resp.raise_for_status()

    keys = resp.json()

    return {idkey['id']: idkey['key'] for idkey in keys}

