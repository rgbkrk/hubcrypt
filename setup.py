#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

# Backwards compatibility for Python 2.x
try:
    from itertools import ifilter
    filter = ifilter
except ImportError:
    pass


def get_version():
    '''
    Version slurping without importing bookstore, since dependencies may not be
    met until setup is run.
    '''
    version_regex = re.compile(r"__version__\s+=\s+"
                               r"['\"](\d+.\d+.\d+[-\w]*)['\"]$")
    versions = filter(version_regex.match, open("hubcrypt/__init__.py"))

    try:
        version = next(versions)
    except StopIteration:
        raise Exception("HubCrypt version not set")

    return version_regex.match(version).group(1)

version = get_version()

packages = [
    'hubcrypt'
]

requires = [
        'requests>=2.1.0',
        'docopt>=0.6.1',
        'PyCrypto>=2.6.1'
]

with open('README.md') as f:
    readme = f.read()
with open('HISTORY.md') as f:
    history = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='hubcrypt',
    version=version,
    description='Encrypt messages using a GitHub user\'s public key.',
    long_description=readme + '\n\n' + history,
    author='Kyle Kelley',
    author_email='rgbkrk@gmail.com',
    url='http://github.com/rgbkrk/hubcrypt',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'hubcrypt': 'hubcrypt'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security :: Cryptography'

    ),
)
