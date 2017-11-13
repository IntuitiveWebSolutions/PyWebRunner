#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  smeggingsmegger
# Purpose: setup
# Created: 2016-06-23
#
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname


long_description = read('README.md')

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='PyWebRunner',
    version='2.0.3',
    url='http://github.com/IntuitiveWebSolutions/PyWebRunner',
    license='MIT',
    author='Scott Blevins',
    author_email='scott@britecore.com',
    description='A library that extends and improves the Selenium python library.',
    long_description=long_description + '\n' + read('CHANGES'),
    platforms='OS Independent',
    packages=['PyWebRunner'],
    data_files=[('extensions', ['JSErrorCollector.xpi', 'JSErrorCollector.crx'])],
    include_package_data=True,
    install_requires=['xvfbwrapper', 'selenium==3.3.0', 'pyaml'],
    keywords=['Selenium', 'Testing'],
    entry_points='''
        [console_scripts]
        webrunner=PyWebRunner.runner:main
    ''',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: User Interfaces",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
