#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import presidial
version = presidial.__version__

setup(
    name='presidial',
    version=version,
    author='',
    author_email='jeremytubbs@gmail.com',
    packages=[
        'presidial',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['presidial/manage.py'],
)
