#!/usr/bin/env python

import os
import sys

import better_requests

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'better_requests',
]

requires = [
    'requests>=1.2.0',
]

setup(
    name='better-requests',
    version=better_requests.__version__,
    description='HTTP for Humans that do right',
    long_description=open('README.md').read(),
    author='better-requests',
    author_email='better-requests@users.noreply.github.com',
    packages=packages,
    package_dir={'better_requests': 'better_requests'},
    package_data={'better_requests': ['LICENSE', 'README.md']},
    include_package_data=True,
    install_requires=requires,
    setup_requires=['setuptools>=38.6.1'],
    license='Apache License v2',
    url='https://github.com/better-requests/better-requests',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
