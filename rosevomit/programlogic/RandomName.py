# ----------------------------------------
# RandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for randomly generating names.

import os
import random
import sys
from inspect import currentframe, getframeinfo

try:
    from core import Directories
except ImportError:  # for external unit testing
    from rosevomit.core import Directories


def one_file (file1):
    """A function that returns one random line from a text file 'x'"""
    data_dir = Directories.get_data_dir()
    os.chdir (data_dir)
    with open (file1, 'r') as fileData:
        contents = fileData.readlines()
        contents = [item.rstrip() for item in contents]  # strips newline characters ('\n') and spaces
        if __name__ != "__main__":
            return (random.choice (contents))
        else:
            print (random.choice (contents))


def two_files (file1, file2):
    """A function that returns one random line from a list generated from multiple text files 'x', 'y', and so on."""
    data_dir = Directories.get_data_dir()
    os.chdir (data_dir)
    fileData1 = open (file1, 'r')
    contents1 = fileData1.readlines()
    contents1 = [item.rstrip() for item in contents1]  # strips newline characters ('\n') and spaces
    fileData1.close()
    fileData2 = open (file2, 'r')
    contents2 = fileData2.readlines()
    contents2 = [item.rstrip() for item in contents2]
    fileData2.close()
    contents = contents1 + contents2
    return (random.choice (contents))


if __name__ == "__main__":
    one_file("SampleData.txt")
