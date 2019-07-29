# --------------------
# WorkWithProgramFiles.py
# --------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for making temp files, saving files, etc.

from inspect import currentframe, getframeinfo
import os
import sys


def CWD_home():
    """Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory"""
    os.chdir (os.path.dirname (sys.argv[0]))


def setname():
    """Determines a valid filename (_filename) for the temp file to be generated. Checks to make sure that _filename is not already in use. If it is, it adds a number on the end of _filename and keeps checking to see if the new _filename is unused, incrementing the number until it finds an unused _filename. """
    _startnum = 1
    _filename = f"log{_startnum}.txt"
    while os.path.isfile (_filename) is True:
        _startnum = _startnum + 1
        _filename = f"log{_startnum}.txt"
    return _filename
