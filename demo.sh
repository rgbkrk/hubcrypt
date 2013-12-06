user=$1
infile=$2
outfile=$2.enc

wget github.com/$user.keys -O id_rsa.pub

# Encrypt
# Need a pem file
ssh-keygen -f id_rsa.pub -e -m PKCS8 > id_rsa.pem.pub # make a pem file
openssl rsautl -encrypt -pubin -inkey id_rsa.pem.pub -ssl -in $infile -out $outfile


## Decrypt
### openssl rsautl -decrypt -inkey ~/.ssh/id_rsa -in totallysecret.txt.enc -out totallysecret.txt # decrypt, yay
