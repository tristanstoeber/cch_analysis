# -*- coding: utf-8 -*-
from setuptools import setup
import os

from setuptools import setup, find_packages

long_description = open("README.md").read()

install_requires = [
    'numpy',
    'collections',
    'matplotlib']
extras_require = {
    'testing': ['pytest'],
    'docs': ['numpydoc>=0.5',
             'sphinx>=1.2.2',
             'sphinx_rtd_theme']
}

setup(
    name="cch_analysis",
    install_requires=install_requires,
    tests_require=install_requires,
    extras_require=extras_require,
    packages=find_packages(),
    include_package_data=True,
    version='0.1',
)