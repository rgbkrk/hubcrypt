hubcrypt
========

Encrypt messages using a GitHub user's public key

Note that hubcrypt chooses the last key listed by default.

# Example Usage

```shell
$ ./hubencrypt.sh smashwilson secrets.txt secrets.txt.enc
Getting the key for smashwilson
Converting public key to a PEM PKCS8 public key
Encrypting message
All done, cleaning up!
```

Later...
```shell
$ ./hubdecrypt.sh ~/.ssh/id_rsa secrets.txt.enc secrets.txt
Enter pass phrase for /home/ash/.ssh/id_rsa:
$ cat secrets.txt
Drink more ovaltine.
```

Also worth noting that messages need to be small enough to actually be able to be encrypted using just public keys. It does of course depend on your key length. For the 2048 bit RSA keys I was using, openssl craps out around 245 bytes. I really wish I knew how these bounds work out mathematically.
