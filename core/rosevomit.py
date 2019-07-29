# --------------------
# ROSEVOMIT.PY
# --------------------
# The main file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python.

print ()
print ("Starting ROSEVOMIT.")
# *** SOME SETUP STUFF ***
# MODULES FROM PYTHON'S STANDARD LIBRARY
print ("Getting some modules from the standard library... ", end="")
try:
    import os
    import pathlib
    import sys
    import textwrap
    import xml.etree.ElementTree as ElementTree
except ImportError as e:
    print ("ERROR.")
    print (f"ERROR INFO: {e}")
    print()
    user_input = input ("Press 'x' to quit, or any other key to continue.")
    user_input = user_input.rstrip()
    if user_input == "x" or user_input == "X":
        SystemExit()
    else:
        pass
else:
    print ("done.")

# MODULES FROM PYPI (the Python community)
# none

# SOME FUNCTIONS AND VARIABLES FOR EASY REFERENCE


def CWD_home():
    """A function to set the current working directory.

    Ensures that the current working directory is set to the home directory of the active script. 
    From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
    """
    os.chdir (os.path.dirname (sys.argv[0]))


def printwrap(x, indented=False, end_with='\n'):
    """Textwrapping for regular 'print' commands."""
    if indented is True:
        print (textwrap.fill (x, width=70, subsequent_indent="   "), end=end_with)
    else:
        print (textwrap.fill (x, width=70), end=end_with)


def main_setup():
    """Contains setup instructions, and prints that info to terminal."""
    print ("Looking for UI, Logic, and Data directories...")
    missingdirectories = []
    CWD_home ()
    with pathlib.Path.cwd() as cwd:
        cli_directory = cwd / 'cli'
        gui_directory = cwd / 'gui'
        logic_directory = cwd / 'logic'
        data_directory = cwd / 'data'

    if os.path.exists (cli_directory):
        print ("   ...CLI directory located.")
    else:
        print ("   ...CLI directory not found.")
        missingdirectories.append("CLI")
    if os.path.exists (gui_directory):
        print ("   ...GUI directory located.")
    else:
        print ("   ...GUI directory not found.")
        missingdirectories.append("GUI")
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

    if os.path.exists (cli_directory) is False or os.path.exists (gui_directory) is False or os.path.exists (logic_directory) is False or os.path.exists (data_directory) is False:
        print (f"I can't find following directories: {missingdirectories}.")
        print ()
        if os.path.exists (gui_directory) is False:
            printw ("The GUI directory is missing, but this program can run perfectly fine from the command-line interface (CLI). User input specifying alternate locations for the UI directory is not supported at this time, but will be added in future versions soon(TM). For now, though, you're stuck with the CLI.")
            print()
            print ("If you would like to exit the program now, enter X or 0.")
            menuchoice = input ("Otherwise, press any key to continue setup. ")
            if menuchoice == '0' or menuchoice == 'X' or menuchoice == "x":
                sys.exit(0)
            else:
                pass
        else:
            printw ("This is a problem - this program will not run properly without a logic or data directory. User input specifying alternate locations for these directories is not supported at this time, but will be added in future versions soon(TM).")
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


def show_main_menu():
    """Contains display instructions for the main menu."""
    print ()
    print (10 * "-", "Rosevomit.py Main Menu", 10 * "-")
    print ("What would you like to generate?")
    print ("     1. Random names")
    print ("     2. A random timeline")
    print ("X or 0. Exit program")
    print ()


def ask_for_input():
    """Asks for user input and processes it. Contains logic for the main menu."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if menuchoice == "1":
        WorseCLI.submenu_name_show()
        WorseCLI.submenu_name_input()
        show_main_menu()
    elif menuchoice == "2":
        WorseCLI.submenu_timeline_show()
        WorseCLI.submenu_timeline_input()
        show_main_menu()
    elif menuchoice == '0' or menuchoice == 'X' or menuchoice == "x" or menuchoice == "exit":
        DialogExit.exit()
        # sys.exit(0)
    elif menuchoice == "help" or menuchoice == "'help'" or menuchoice == "h" or menuchoice == "H" or menuchoice == "helf":
        show_main_menu()
    elif menuchoice == "":
        ask_for_input()
    else:
        print (f"{menuchoice} is not a recognized command.")


# **********************************************
# ********** MAIN PROGRAM STARTS HERE **********
# **********************************************

main_setup()
print ("Proceeding to get local modules... ", end="")
CWD_home()
from logic import LogicController
from cli import DialogExit, TextStuff, WorseCLI
print ("done.")

print ()
print (69 * "-")
print (27 * "-", "ROSEVOMIT.PY", 28 * "-")
print (69 * "-")
print ()

# After setup, rosevomit.py will display the main menu and will carry out instructions based on user input. This is an infinite loop - if rosevomit.py ever has no more instructions to carry out, it displays the main menu again and awaits further instructions. This is based on the 'see_rosa_run' variable. This variable should never change. If it does, the program exits and gives the system an error code.
see_rosa_run = True
show_main_menu()
while see_rosa_run is True:
    ask_for_input()
else:
    sys.exit(1)
