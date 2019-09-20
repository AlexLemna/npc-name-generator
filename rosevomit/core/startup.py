# --------------------
# Startup.PY
# --------------------
# The setup utility file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python.
from distutils.util import strtobool
import os
import pathlib
import sys
import xml.etree.ElementTree as ElementTree

from core.utilities import debugmessage
from programcli.textstuff import printwrap


def main_setup(homedir):
    """Contains setup instructions, and prints that info to terminal."""
    debugmessage ("Looking for UI, Logic, and Data directories...")
    missingdirectories = []
    homedir = pathlib.Path(homedir)
    cli_directory = homedir / 'programcli'
    logic_directory = homedir / 'programlogic'
    data_directory = homedir / 'programdata'
    temp_directory = homedir / 'temp'

    # determining if we've got all our directories where we expect them to be
    if os.path.exists (cli_directory):
        debugmessage ("   ...CLI directory located.")
    else:
        debugmessage ("   ...CLI directory not found.")
        missingdirectories.append("CLI")
    if os.path.exists (logic_directory):
        debugmessage ("   ...logic directory located.")
    else:
        debugmessage ("   ...logic directory not found.")
        missingdirectories.append("Logic")
    if os.path.exists (data_directory):
        debugmessage ("   ...data directory located.")
    else:
        debugmessage ("   ...data directory not found.")
        missingdirectories.append("Data")
    if os.path.exists(temp_directory):
        debugmessage ("   ...temp directory located.")
    else:
        debugmessage (f"   ...temp directory not found. A new temp directory will be created in '{homedir}'... ", indented=True, end_with="")
        os.mkdir ("temp")
        debugmessage ("done.")

    # let the user know whether or not we've got all the necessary directories
    if os.path.exists (cli_directory) is False or os.path.exists (logic_directory) is False or os.path.exists (data_directory) is False:
        print (f"I can't find following directories: {missingdirectories}.")
        print ()
        printwrap ("This is a problem - this program will not run properly without these directories. User input specifying alternate locations for these directories is not supported at this time, but will be added in future versions soon(TM).")
        input ("Press any key to quit.")
        sys.exit(1)
    else:
        debugmessage ("All directories present.")
    print("Main setup complete. Getting version number... ", end="")
    try:
        os.chdir (data_directory)
        tree = ElementTree.parse ("Version.xml")
        root = tree.getroot()
        human_version = root.findall("./version[@type='human']//")
        for child in human_version:
            if child.tag == "major":
                major_version = child.text
            elif child.tag == "minor":
                minor_version = child.text
            elif child.tag == "patch":
                patch_version = child.text
            else:
                raise IOError
        released = root.findtext("released", default=True)
        released = strtobool (released)  # Because the 'findtext' function above returns a string, not a bool.
        print ("done.")
        print()
        if not released:
            print (f"You are using a development build of Rosevomit {major_version}.{minor_version}.{patch_version}. This")
            print ("software is actively under development, and this development")
            print ("build may not be stable! Proceed at your own risk.")
        else:
            print (f"You are using Rosevomit {major_version}.{minor_version}.{patch_version}. This software is")
            print ("actively under development. Proceed at your own risk.")
    except FileNotFoundError:
        print ("ERROR.")
        print ("COULD NOT FIND VERSION FILE.")
    except IOError:
        print ("ERROR.")
        print ("VERSION FILE IS INCOMPLETE OR FORMATTED INCORRECTLY.")
    print()
    print ("Press any key to accept risk and continue, or")
    print ("end the program by exiting this window.")
    input()
    print()
