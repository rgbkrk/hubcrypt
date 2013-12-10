# CryptHub

[![Build Status](https://magnum.travis-ci.com/rgbkrk/hubcrypt.png?token=zrnzC1rKNTsStESZRWcJ&branch=master)](https://magnum.travis-ci.com/rgbkrk/hubcrypt)

:closed_lock_with_key: for your :octocat:

## Summary

Encrypt [\*](https://github.com/rgbkrk/hubcrypt/blob/master/README.md#-maximum-message-size-is-based-on-key-size)short messages using a GitHub user's public key.

### Encryption:

```shell
$ ./bin/hubencrypt smashwilson secrets.txt secrets.txt.enc
Getting the key for smashwilson
Converting public key to a PEM PKCS8 public key
Encrypting message
All done, cleaning up!
```

### Decryption:

```shell
$ ./bin/hubdecrypt ~/.ssh/id_rsa secrets.txt.enc secrets.txt
Enter pass phrase for /home/ash/.ssh/id_rsa:
$ cat secrets.txt
Drink more ovaltine.
```

## About

hubcrypt relies on the fact that you (probably) already have public and private keypairs, the public keys of which are readily accessible through GitHub's API. You use them to push code and log in to servers. They're not limited to those tasks though, as they can be used to encrypt arbitrary data.

Normally public keys are used to encrypt a randomly generated session key for use with a symmetric encryption algorithm. The big reason is that asymmetric encryption is typically much slower than symmetric encryption. [PGP](http://en.wikipedia.org/wiki/Pretty_Good_Privacy#Design) for instance uses this exact scheme.

Jokingly, I said to someone that if they wanted to share a small secret with another GitHub user they could just encrypt them with their public SSH key. So, [hubcrypt was born as a gist](https://gist.github.com/rgbkrk/7827691).

Shortly after I found out that [others](https://github.com/twe4ked/catacomb) had done [variations on this](https://github.com/jschauma/jass) before. Not surprised, I'm always late to the party.

You could of course use GPG and convince the other person you're communicating with to use GPG as well. Or you could just use the SSH keys you already have to encrypt a message. Sure beats sending it over plain.

## Requirements

The recipient needs to be using an RSA key and have it listed as the last key on `github.com/<user>.keys`. Linux and OS X before Mavericks should work well.

If your machine doesn't support ssh-keygen properly, submit an issue and I'll bemoan that I don't have a box to test it on for you. Feel free to send us a brand new laptop to test your flavor of operating system with.

## Example Usage

```shell
$ git clone https://github.com/rgbkrk/hubcrypt.git
$ ./hubcrypt/bin/hubencrypt smashwilson secrets.txt secrets.txt.enc
Getting the key for smashwilson
Converting public key to a PEM PKCS8 public key
Encrypting message
All done, cleaning up!
```

Later, on [smashwilson](https://github.com/smashwilson)'s computer:

```shell
$ git clone https://github.com/rgbkrk/hubcrypt.git
$ ./hubcrypt/bin/hubdecrypt ~/.ssh/id_rsa secrets.txt.enc secrets.txt
Enter pass phrase for /home/ash/.ssh/id_rsa:
$ cat secrets.txt
Drink more ovaltine.
```

You can copy the shell scripts to wherever you like, then it's simply a matter of running `hubencrypt` and `hubdecrypt`.

Alternatively, just steal the `openssl` and `ssh-keygen` commands and roll like a boss. You will miss out on the ever so insightful error messages.

## \* Maximum Message size (is based on key size)

The typical key size when people run `ssh-keygen` is 2048 bits. You can make that beefier or leaner at your own discretion. The user's choice in keysize affects the size of the message you can send them.

```
Key size (bits)    Maximum Message Size (bytes)
768                                          85
1024                                        117
2048                                        246
4096                                        502
8192                                       1018
```


