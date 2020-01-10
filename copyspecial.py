#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "cdanjha"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    cmd = 'ls -l ' + dir

    (status, output) = subprocess.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    sfiles = re.findall(r'\w+[_]\.\w+', output)
    spaths = map(lambda x: os.path.abspath(
        os.path.join(dir, x)), sfiles)
    return spaths

def copy_to(paths, dir):
    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(os.path.abspath(dir))
    for path in paths:
        shutil.copy(path, os.path.abspath(dir))

def zip_to(paths, zippath):
    cmd = 'zip -j {} '.format(zippath) + " ".join(paths)
    (status, output) = subprocess.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print(output)

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    #args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    parser.add_argument('from_dir', help='origin dir for special files')
    results = parser.parse_args()
    if not results:
        parser.print_usage()
        sys.exit(1)
    todir = results.todir
    from_dir = results.from_dir
    tozip = results.tozip
    spaths = get_special_paths(from_dir)
    if todir:
        copy_to(spaths, todir)
    elif tozip:
        zip_to(spaths, tozip)
    else:
        print("\n".join(spaths))

if __name__ == "__main__":
    main()
