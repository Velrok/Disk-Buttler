#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Disk Buttler.
Reads directory from source_dir
and creates empty folders in the destination_dir.

Usage:
    disk_buttler.py <source_dir> <destination_dir>

"""
import os
from docopt import *


def mirror_dir(src, dst):
    # like an ls call
    src_content = os.listdir(src)

    only_dir_names = []
    for src_element in src_content:
        # combine the user src path with subfolder to a full path,
        # so path.isdir can check if it is dir or not
        fullpath = os.path.join(src, src_element)
        #check if path end with dir or file and write dirs into "only_dir_names"
        if os.path.isdir(fullpath):
            only_dir_names.append(src_element)

    #generate folder in dst path based on only_dir_names
    for dst_element in only_dir_names:
        dst_path = os.path.join(dst, dst_element)
        os.mkdir(dst_path)


if __name__ == '__main__':
    args = docopt(__doc__)
    src = arguments["<source_dir>"]
    dst = arguments["<destination_dir>"]

    mirror_dir(src, dst)

    # also mirror the Serien subfolder
    # TODO: make this configurable
    src_serien = os.path.join(src, "Serien")
    dst_serien = os.path.join(dst, "Serien")

    mirror_dir(src_serien, dst_serien)
