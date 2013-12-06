#!/usr/bin/env bash

key=$1
infile=$2
outfile=$3

openssl rsautl -decrypt -inkey $key -in $infile -out $outfile
