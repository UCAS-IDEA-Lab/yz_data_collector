#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os, sys

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(HERE, 'yz_agent'))

def main():
    setup_args = dict(
        name="yz_agent",
        version="0.5.1",
        description="Data collect agent",
        author="CannedFish Liang",
        author_email="lianggy0719@126.com",
        url="https://github.com/CannedFish/yz_data_collector",
        platforms="Linux",
        license="BSD",
        packages=find_packages(),
        install_requires=['web.py==0.38', 'requests>=2.7.0', 'protobuf==3.3.0'],
        package_data={},
        entry_points={
            'console_scripts': [
                'yz_agent = yz_agent.main:main',
                'yz_test_data_gen = yz_agent.test.data_gen:main'
            ]
        }
    )
    setup(**setup_args)

if __name__ == '__main__':
    main()

