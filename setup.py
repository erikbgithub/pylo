#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Hello World Test project
#
# Copyright (C) 2013 Erik Bernoth, erik.bernoth@gmail.com
#
# Do whatever you want with this.

from distutils.core import setup

setup(
    name="pylo",
    version="1.0",
    description="A project to test all kind of stuff",
    author="Erik Bernoth",
    author_email="erik.bernoth@gmail.com",
    url="https://github.com/erikb85/pylo",
    packages=["pylo"],
    package_dir={"":"src"},
    provides=["pylo (1.0)"]
)

