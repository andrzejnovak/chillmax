#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
from setuptools import (
    setup,
    find_packages,
)


about = {}
with open(os.path.join("chillmax", "version.py")) as f:
    exec(f.read(), about)


needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

setup(name="chillmax",
      version=about["__version__"],
      packages=find_packages(),
      scripts=[],
      include_package_data=True,
      description="",
      long_description=open("README.md", "rb").read().decode("utf8", "ignore"),
      long_description_content_type="text/markdown",
      maintainer="Andrzej Novak",
      maintainer_email="andrzej.novak@cern.ch",
      url="https://github.com/andrzejnovak/chillmax",
      download_url="",
      license="BSD 3-clause",
      test_suite="tests",
      install_requires=[
          "numpy>=1.14",
      ],
      setup_requires=["flake8"] + pytest_runner,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Topic :: Scientific/Engineering :: Physics",
      ],
      )
