# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='huffman-encode',
    version='0.1.0',
    description='huffman-encoder package to reduce data based on character frequency',
    long_description=readme,
    author='Maverick Perrollaz',
    author_email='maverick.perrollaz@pm.me',
    url='https://github.com/M4verickFr/huffman-encode',
    license=license,
    packages=find_packages()
)
