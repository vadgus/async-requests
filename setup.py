#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

extra = {}
if sys.version_info >= (3, 4):
    extra['use_2to3'] = False
    extra['convert_2to3_doctests'] = ['README.md']

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(name='async-requests',
      version="0.0.1",
      description="""many async requests sender""",
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author="Vadim Gusyatnikov",
      author_email="guva.gurtam@gmail.com",
      url='https://github.com/vadgus/async-requests',
      packages=find_packages(),
      download_url='https://github.com/vadgus/async-requests',
      classifiers=CLASSIFIERS,
      keywords='many async requests sender',
      zip_safe=True,
      install_requires=[],
      tests_requires=[
          'pytest==3.8.0',
          'pytest-cov==2.6.0',
          'pytest-asyncio==0.9.0',
      ]
      )
