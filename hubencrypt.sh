#!/usr/bin/env bash

# Encrypts a small message (< 245 bytes) using a github user's public key as
# pulled from github.com/<user>.keys

# This is silliness, don't use it in production

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

wget github.com/$user.keys --quiet -qO- > $pubkey #-O $pubkey
#wget github.com/$user.keys --quiet -qO- | tail -n 1 > $pubkey #-O $pubkey

# Need a pem file, so we convert it
ssh-keygen -f $pubkey -e -m PKCS8 > $pubkey.pem
openssl rsautl -encrypt -pubin -inkey $pubkey.pem -ssl -in $infile -out $outfile

# Clean up
rm $pubkey
rm $pubkey.pem
