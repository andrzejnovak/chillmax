#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
from setuptools import find_packages, setup
from setuptools.command.install import install

about = {}
with open(os.path.join("chillmax", "version.py")) as f:
    exec(f.read(), about)

INSTALL_REQUIRES = [
    "numpy>=1.16.0",
    "scipy>=1.1.0",
    "requests~=2.21",
    "packaging",
]

extras_require = {
    "test": ["pytest", "papermill~=1.0",],
    "develop": ["flake8"],
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(
    name="chillmax",
    version=about["__version__"],
    scripts=[],
    packages=find_packages(),
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
    install_requires=INSTALL_REQUIRES,
    extras_require=extras_require,
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
