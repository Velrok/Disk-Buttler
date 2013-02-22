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


# See http://docs.python.org/library/argparse.html#module-argparse
def parse_args():
    # create a argument parser from the library
    args_parser = argparse.ArgumentParser(description='Disk Buttler')

    # 1st argument is the source directory
    args_parser.add_argument('source',
        type=str,
        help='directory to read the subfolder names from')

    # 2nd argument is the source directory
    args_parser.add_argument('destination',
        type=str,
        help='directory where the new empty subfolders should be created')

    return args_parser.parse_args()


def mirror_dir(src, dst):
    #create a list containing src subfolder foldernames
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
