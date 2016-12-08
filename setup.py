#!/usr/bin/env python3

import io
from setuptools import find_packages, setup

def long_desc():
    with io.open("README.md") as f:
        readme = f.read()
    return readme

setup(name = "match",
      description = "",
      long_description = long_desc(),
      url = "https://github.com/jonsafari/match",
      author = "Jon Dehdari",
      author_email = "jon@dehdari.org",
      license = "GNU Lesser General Public License v3",
      install_requires=['numpy'],
      packages = find_packages(),
      classifiers = ["Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.4",
                     "Programming Language :: Python :: 3.5",
                     'Operating System :: OS Independent',
                    ],
      zip_safe = False
     )
