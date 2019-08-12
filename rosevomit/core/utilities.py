# rosevomit/core/Utilities.py
# For those little code snippets that don't make sense going anywhere else.
import os
import sys
import textwrap

from core import settings


def CWD_home():
    """Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory"""
    os.chdir (os.path.dirname (sys.argv[0]))


def debugmessage(debugstring: str, **kwargs):
    is_debugging_on: bool = settings.debug_startup()
    if is_debugging_on is True:
        print (textwrap.fill (debugstring), **kwargs)
    else:
        pass
