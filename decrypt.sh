#!/usr/bin/env bash

if [[ $# < 3 ]]; then
  echo "Usage: $0 <id_rsa> <infile> <outfile>"
fi

key=$1
infile=$2
outfile=$3

openssl rsautl -decrypt -inkey $key -in $infile -out $outfile
