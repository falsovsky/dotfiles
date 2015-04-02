#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import json
import sys

home = os.path.expanduser("~")
dotfiles = os.path.dirname(os.path.realpath(sys.argv[0]))

with open('symlinks.json') as data_file:    
    symlinks = json.load(data_file)

for symlink in symlinks:
    src = os.path.join(dotfiles, symlink)
    dst = os.path.join(home, symlinks[symlink])
    print(src + " -> " + dst)
    if (os.path.islink(dst)):
        print("Already a symlink, ignoring...")
        continue
    if (os.path.isfile(dst)):
        print("Is a file, ignoring...")
        continue
    os.symlink(src, dst)

