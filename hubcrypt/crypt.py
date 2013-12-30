#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Crypto.PublicKey.RSA as RSA

def convert_key(ssh_key):
    '''
    Pass in a public SSH key, get a PEM key back that follows PKCS standard #1.

    >>> pub_key = "ssh-rsa
    ... AAAAB3NzaC1yc2EAAAADAQABAAABAQDRkGTt3IW4snceuvep4scqRPx1IHPd7pRblLb611mcBb5Yo12jjp6vnyEhvxrSY85HVDXK4q7voeG1zTwAmeD7iJ2WeXi5a42UclVBcTxG1QePrFvv9NcZlNz39J9utfs8Hf+RPbMpa0FWw9+0Q9X8SPaQkmUQKnlBm29lYS7S/DWfowF0vu6jOaFJHECIgSA4WbudjVQyDTNvzcffdocMc1z5YaGSDuslK7OafZA1aDRWghU1vNUcP2ZN0h3JfGt56WauukJU19ZNuuIl25EgPuPTFLlq11Agp3p5cVpfo+Fym9ghCzzavxPKfeqGjrxq/dwBxH9MN85g3dSAM8b3"
    >>> convert_key(pub_key)
    '''
    rsa_key = RSA.importKey(ssh_key)
    return rsa_key.exportKey('PEM', pkcs=1)

def encrypt(public_key, message):
    '''
    Encrypts a message using the given public key in PEM PKCS#1 format

    >>> cipher = encrypt(public_key, "Drink more ovaltine.")
    '''
    #openssl rsautl -encrypt -pubin -inkey $pubkey.pem -ssl -in $infile -out $outfile
    pass
