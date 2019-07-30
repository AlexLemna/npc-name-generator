# --------------------
# Startup.PY
# --------------------
# The setup utility file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python.
import os
import pathlib
import sys
import textwrap
import xml.etree.ElementTree as ElementTree

from programcli.TextStuff import printwrap


def CWD_home():
    """A function to set the current working directory.

    Ensures that the current working directory is set to the home directory of the active script.
    From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
    """
    os.chdir (os.path.dirname (sys.argv[0]))


def main_setup():
    """Contains setup instructions, and prints that info to terminal."""
    print ("Looking for UI, Logic, and Data directories...")
    missingdirectories = []
    CWD_home ()
    with pathlib.Path.cwd() as cwd:
        cli_directory = cwd / 'programcli'
        logic_directory = cwd / 'programlogic'
        data_directory = cwd / 'programdata'
        temp_directory = cwd / 'temp'

    # determining if we've got all our directories where we expect them to be
    if os.path.exists (cli_directory):
        print ("   ...CLI directory located.")
    else:
        print ("   ...CLI directory not found.")
        missingdirectories.append("CLI")
    if os.path.exists (logic_directory):
        print ("   ...logic directory located.")
    else:
        print ("   ...logic directory not found.")
        missingdirectories.append("Logic")
    if os.path.exists (data_directory):
        print ("   ...data directory located.")
    else:
        print ("   ...data directory not found.")
        missingdirectories.append("Data")
    if os.path.exists(temp_directory):
        print ("   ...temp directory located.")
    else:
        printwrap (f"   ...temp directory not found. A new temp directory will be created in '{cwd}'... ", indented=True, end_with="")
        os.mkdir ("temp")
        print ("done.")

    # let the user know whether or not we've got all the necessary directories
    if os.path.exists (cli_directory) is False or os.path.exists (logic_directory) is False or os.path.exists (data_directory) is False:
        print (f"I can't find following directories: {missingdirectories}.")
        print ()
        printwrap ("This is a problem - this program will not run properly without these directories. User input specifying alternate locations for these directories is not supported at this time, but will be added in future versions soon(TM).")
        input ("Press any key to quit.")
        sys.exit(1)
    else:
        print ("All directories present.")
    print("Main setup complete. Getting version number... ", end="")
    try:
        os.chdir (data_directory)
        tree = ElementTree.parse ("Version.xml")
        root = tree.getroot()
        treeHumanVersion = root.findall("./version[@type='human']//")
        for child in treeHumanVersion:
            if child.tag == "major":
                major_version = child.text
            elif child.tag == "minor":
                minor_version = child.text
            elif child.tag == "patch":
                patch_version = child.text
            else:
                raise IOError
        print ("done.")
        print()
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
