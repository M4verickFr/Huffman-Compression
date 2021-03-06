# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='huffman-project',
    version='0.1.0',
    description='huffman-project package to reduce data based on character frequency',
    long_description=readme,
    author='Maverick Perrollaz',
    author_email='maverick.perrollaz@pm.me',
    url='https://github.com/M4verickFr/huffman-project',
    license=license,
    packages=find_packages()
)
