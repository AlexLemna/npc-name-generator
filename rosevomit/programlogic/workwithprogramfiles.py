# --------------------
# WorkWithProgramFiles.py
# --------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for making temp files, saving files, etc.

import os


def setname(ARG_basename):
    """Determines a valid filename for based off a desired 'ARG_basename'. Checks to make sure that _filename is not already in use. If it is, it adds a number on the end of _filename and keeps checking to see if the new _filename is unused, incrementing the number until it finds an unused _filename. """
    _startnum = 1
    _filename = f"{ARG_basename}{_startnum}.txt"
    while os.path.isfile (_filename) is True:
        _startnum = _startnum + 1
        _filename = f"{ARG_basename}{_startnum}.txt"
    return _filename
