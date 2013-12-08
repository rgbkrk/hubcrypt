#!/usr/bin/env bash

#
# HubCrypt
# ========
#
# Encrypts a small message using a github user's public key as pulled from
# github.com/<user>.keys
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
# these ranges.
#
# Note: This assumes that the key is an RSA public key, and that the public
#       key you want to use is the first one listed at github.com/<user>.keys
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

# Grab the first key because why not?
wget github.com/$user.keys --quiet -qO- | head -n 1 > $pubkey #-O $pubkey
#wget github.com/$user.keys --quiet -qO- | tail -n 1 > $pubkey #-O $pubkey

# Need a pem file, so we convert it
ssh-keygen -f $pubkey -e -m PKCS8 > $pubkey.pem
openssl rsautl -encrypt -pubin -inkey $pubkey.pem -ssl -in $infile -out $outfile

# Clean up
rm $pubkey
rm $pubkey.pem
