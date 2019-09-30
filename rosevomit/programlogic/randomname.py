# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# randomname.py
# rosevomit.programlogic.randomname
# ___________________________________________________________________
"""A file that contains functions for randomly generating names."""

import os
import random

try:
    from core import directories
except ImportError:  # for external unit testing
    from rosevomit.core import directories


def one_file (ARG_file1) -> str:
    """A function that returns one random line from a text file 'x'"""
    data_dir = directories.get_dir("programdata")
    os.chdir (data_dir)
    with open (ARG_file1, 'r') as filedata:
        contents = filedata.readlines()
        contents = [item.strip() for item in contents]  # strips newline characters ('\n') and spaces
        return random.choice (contents)


def two_files (ARG_file1, ARG_file2) -> str:
    """A function that returns one random line from a list generated from multiple text files 'x', 'y', and so on."""
    data_dir = directories.get_dir("programdata")
    os.chdir (data_dir)
    filedata1 = open (ARG_file1, 'r')
    contents1 = filedata1.readlines()
    contents1 = [item.strip() for item in contents1]  # strips newline characters ('\n') and spaces
    filedata1.close()
    filedata2 = open (ARG_file2, 'r')
    contents2 = filedata2.readlines()
    contents2 = [item.strip() for item in contents2]
    filedata2.close()
    contents = contents1 + contents2
    return random.choice (contents)


def getname_firstany():
    """Returns a random first name."""
    result = two_files ("USCensusNamesFirstFemale.txt", "USCensusNamesFirstMale.txt")
    print (result)


def getname_firstfemale():
    """Returns a random female first name."""
    result = one_file ("USCensusNamesFirstFemale.txt")
    print (result)


def getname_firstmale():
    """Returns a random male first name."""
    result = one_file ("USCensusNamesFirstMale.txt")
    print (result)


def getname_lastany():
    """Returns a random last name."""
    result = one_file ("USCensusNamesLast.txt")
    print (result)


def getname_fullany():
    """Returns a random full name."""
    firstname = two_files ("USCensusNamesFirstFemale.txt", "USCensusNamesFirstMale.txt")
    lastname = one_file ("USCensusNamesLast.txt")
    result = firstname + lastname
    print (result)


def getname_fullfemale():
    """Returns a random female full name."""
    firstname = one_file ("USCensusNamesFirstFemale.txt")
    lastname = one_file ("USCensusNamesLast.txt")
    result = firstname + lastname
    print (result)


def getname_fullmale():
    """Returns a random male full name."""
    firstname = one_file ("USCensusNamesFirstMale.txt")
    lastname = one_file ("USCensusNamesLast.txt")
    result = firstname + lastname
    print (result)
