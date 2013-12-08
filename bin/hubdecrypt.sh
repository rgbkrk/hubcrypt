#!/usr/bin/env bash

#
# Decrypt a file encrypted using hubencrypt (ok, it's just openssl + rsautl +
# your SSH keys). It needs the private key that matches your last public key
# listed at github.com/<user>.keys

# Note that this is silliness and shouldn't be used in production.

if [[ $# < 3 ]]; then
  echo "Usage: $0 <id_rsa> <infile> <outfile>"
  exit 1
fi

key=$1
infile=$2
outfile=$3

openssl rsautl -decrypt -inkey $key -in $infile -out $outfile
