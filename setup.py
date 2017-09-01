#! /usr/bin/env python

from setuptools import setup, find_packages
import sys
import os

VERSION = '0.1.0'


def main():
    setup(name='pysyncr',
          version=VERSION,
          description="Upload, download or sync photos and videos to flickr",
          long_description=open('README.txt').read(),
          classifiers=[
              'Development Status :: 3 - Alpha',
              'Environment :: Console',
              'Programming Language :: Python',
              'License :: OSI Approved :: MIT License'
          ],
          keywords='flickr upload download sync photos images videos backup',
          url='https://github.com/antocuni/pysyncr',
          license='MIT',
          packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
          include_package_data=True,
          zip_safe=False,
          install_requires=['watchdog', 'IPTCInfo', 'six', 'requests_toolbelt', 'requests_oauthlib', 'pyyaml', 'flickrapi'],
          entry_points={
              "console_scripts": ['pysyncr = pysyncr:main'],
          },
          )

if __name__ == '__main__':
    main()
