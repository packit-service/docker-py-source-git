#!/usr/bin/env python
from __future__ import print_function

import codecs
import os
import sys

from setuptools import find_packages
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

requirements = [
    'six >= 1.4.0',
    'websocket-client >= 0.32.0',
    'requests >= 2.14.2, != 2.18.0',
]

if sys.version_info[:2] < (3, 5):
    requirements.append('backports.ssl_match_hostname >= 3.5')
# While not imported explicitly, the ipaddress module is required for
# ssl_match_hostname to verify hosts match with certificates via
# ServerAltname: https://pypi.python.org/pypi/backports.ssl_match_hostname
if sys.version_info[:2] < (3, 3):
    requirements.append('ipaddress >= 1.0.16')

version = None
exec(open('docker/version.py').read())

with open('./test-requirements.txt') as test_reqs_txt:
    test_requirements = [line for line in test_reqs_txt]


long_description = ''
with codecs.open('./README.md', encoding='utf-8') as readme_md:
    long_description = readme_md.read()

setup(
    name="docker",
    version=version,
    description="A Python library for the Docker Engine API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/docker/docker-py',
    project_urls={
        'Documentation': 'https://docker-py.readthedocs.io',
        'Changelog': 'https://docker-py.readthedocs.io/en/stable/change-log.html',  # noqa: E501
        'Source': 'https://github.com/docker/docker-py',
        'Tracker': 'https://github.com/docker/docker-py/issues',
    },
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=requirements,
    tests_require=test_requirements,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
    maintainer='Joffrey F',
    maintainer_email='joffrey@docker.com',
)
