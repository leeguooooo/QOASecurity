#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='QOASecurityUtil',
    version='1.1.1',
    description=(
        'QOAToken工具'
    ),
    long_description=open('README.rst').read(),
    author='lee.guo',
    author_email='leeguoo@163.com',
    maintainer='lee.guo',
    maintainer_email='leeguoo@163.com',
    license='BSD License',
    packages=['QOASecurityUtil'],
    platforms=["all"],
    url='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
