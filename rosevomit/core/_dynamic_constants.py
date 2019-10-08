# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# _dynamic_constants.py
# rosevomit.core._dynamic_constants
# ___________________________________________________________________
"""This file contains the functions that generate the dynamic constants."""
from distutils.util import strtobool
import os
import pathlib
from xml.etree import ElementTree

from core import directories
from core.utilities import debugmessage


def get_critical_directory (ARG_dirname: str) -> pathlib.Path:
    """Tries to find the path to a directory. If the path cannot be found, this function will *not* surpress any exceptions and will *not* attempt to create a directory on its own.

    Basically, this function is just a wrapper for core.directories.get_dir().
    """
    _result = directories.get_dir (ARG_dirname)
    return _result


def get_noncritical_directory (ARG_dirname: str) -> pathlib.Path:
    """Tries to find the path to a directory. If the path cannot be found, this function will *not* surpress any exceptions and will *not* attempt to create a directory on its own.

    Basically, this function is just a wrapper for core.directories.get_dir().
    """
    try:
        _result = directories.get_dir (ARG_dirname)
    except (FileNotFoundError, ValueError) as e:
        debugmessage (e)
        _result = None
    return _result


def get_version_number(ARG_core_directory: pathlib.Path):
    """Gets the version number."""
    try:
        debugmessage ("Getting version number...", end=" ")
        os.chdir (ARG_core_directory)
        _tree = ElementTree.parse ("Version.xml")
        _root = _tree.getroot ()
        _human_version = _root.findall("./version[@type='human']//")
        for child in _human_version:
            if child.tag == "major":
                major_version = child.text
            elif child.tag == "minor":
                minor_version = child.text
            elif child.tag == "patch":
                patch_version = child.text
            else:
                raise IOError
        _devbuild = _root.findtext("devbuild", default="False")
        _devbuild = strtobool (_devbuild)  # Because the 'findtext' function above returns a string, not a bool. pylint: disable=invalid-name
        is_devbuild = bool (_devbuild)  # And because, despite its name, 'strtobool()' returns an integer (1 or 0), not a bool
        debugmessage ("done.")
    except FileNotFoundError:
        debugmessage ("error.")
        print ("ERROR: COULD NOT FIND VERSION FILE.")
    except IOError:
        debugmessage ("error.")
        print ("ERROR: VERSION FILE IS INCOMPLETE OR FORMATTED INCORRECTLY.")
    else:
        return major_version, minor_version, patch_version, is_devbuild
