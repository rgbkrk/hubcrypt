#!/usr/bin/env bash

#
# HubCrypt
# ========
#
# Encrypts a small message using a github user's public key as pulled from
# github.com/<user>.key (ok, the last public key listed).
#
# The message size you can encrypt depends on the size of the RSA key used.
#
# Key size (bits)    Maximum Message Size (bytes)
# 768                                          85
# 1024                                        117
# 2048                                        246
# 4096                                        502
# 8192                                       1018
#
# The key size (as specified by `-b` when using ssh-keygen) doesn't actually
# have to be a power of 2, and will give you maximum message sizes in between
# these ranges. I leave that as an exercise to the reader. If you want the
# "solution" email me. Or leave a message on the gist this originally came from.
# Whatever.
#
# Note: This assumes that the key is an RSA public key, and that the public
#       key you want to use is the last one listed at github.com/<user>.keys
#
#       Also, this is silliness, don't use it in production

if [[ $# < 2 ]]; then
  echo "Usage: $0 <github user> <infile> [outfile]"
  exit 1
fi

user=$1
infile=$2
outfile=$2.enc

if [[ $# == 3 ]]; then
  outfile=$3
fi

pubkey=/tmp/$user.$RANDOM.pub

echo "Getting the key for $user"

# Grab the first key because why not?
#wget github.com/$user.keys --quiet -qO- | head -n 1 > $pubkey #-O $pubkey
# Grab the last key because they added it last
wget github.com/$user.keys --quiet -qO- | tail -n 1 > $pubkey #-O $pubkey

# Need a pem file, so we convert it
echo "Converting public key to a PEM PKCS8 public key"
ssh-keygen -f $pubkey -e -m PKCS8 > $pubkey.pem

if [[ $? != 0 ]]; then
  print "Since there was an error creating the public key, we'll exit"
  exit 1
fi

echo "Encrypting message"
openssl rsautl -encrypt -pubin -inkey $pubkey.pem -ssl -in $infile -out $outfile

if [[ $? != 0 ]]; then
  print "OpenSSL failed. No encrypting your message."
  exit 1
fi

echo "All done, cleaning up!"

# Clean up
rm $pubkey
rm $pubkey.pem
