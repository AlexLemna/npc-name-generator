# ----------------------------------------
# RandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for randomly generating names.

import os
import random

try:
    from core import directories
except ImportError:  # for external unit testing
    from rosevomit.core import directories


def one_file (file1) -> str:
    """A function that returns one random line from a text file 'x'"""
    data_dir = directories.get_dir("programdata")
    os.chdir (data_dir)
    with open (file1, 'r') as filedata:
        contents = filedata.readlines()
        contents = [item.strip() for item in contents]  # strips newline characters ('\n') and spaces
        return random.choice (contents)


def two_files (file1, file2) -> str:
    """A function that returns one random line from a list generated from multiple text files 'x', 'y', and so on."""
    data_dir = directories.get_dir("programdata")
    os.chdir (data_dir)
    filedata1 = open (file1, 'r')
    contents1 = filedata1.readlines()
    contents1 = [item.strip() for item in contents1]  # strips newline characters ('\n') and spaces
    filedata1.close()
    filedata2 = open (file2, 'r')
    contents2 = filedata2.readlines()
    contents2 = [item.strip() for item in contents2]
    filedata2.close()
    contents = contents1 + contents2
    return random.choice (contents)
