#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import json

with open('symlinks.json') as data_file:    
    symlinks = json.load(data_file)
