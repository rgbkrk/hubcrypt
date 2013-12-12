#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HubCrypt

Encrypt a message for a GitHub user.

Usage:
    hubcrypt encrypt <username> - [options]
    hubcrypt encrypt <username> --message=plaintext [options]
    hubcrypt encrypt <username> --in=plainfile [options]

Options:
    -h --help             Show this help message.
    --version             Show version.
    --id=<key_id>         Use the key ID instead of all of them
    --endpoint=<endpoint> GitHub site to pull keys from [default: https://api.github.com/]
                          (For example: use with GitHub enterprise)
    --send                Send message to crypthub.io
    --out=<outfile>       Write output to outfile

"""

from docopt import docopt

import hubcrypt

if __name__ == "__main__":
    args = docopt(__doc__, version=hubcrypt.__version__)

    print(args)


