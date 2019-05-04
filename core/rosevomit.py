# --------------------
# ROSEVOMIT.PY
# --------------------
# The main file for Alex's "Project ROSEVOMIT", a random name generator written in Python.

# *** SOME SETUP STUFF ***
# MODULES FROM PYTHON'S STANDARD LIBRARY
print ("Getting some modules from the standard library... ", end="")
import os
import pathlib
import sys
import textwrap
print ("done.")

# MODULES FROM PYPI (the Python community)
# none



# SOME FUNCTIONS AND VARIABLES FOR EASY REFERENCE
def CWD_home():
    '''A function to set the current working directory.

    Ensures that the current working directory is set to 
    the home directory of the active script. From 
    https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
    '''
    os.chdir (os.path.dirname (sys.argv[0]))

def printw(x): 
    '''Textwrapping for regular 'print' commands.'''
    print ( textwrap.fill (x, width = 70))

def RosevomitSetup(): # Contains setup instructions.
    print ("Looking for UI, Logic, and Data directories...")
    missingDirectories = []
    CWD_home ()
    with pathlib.Path.cwd() as cwd:
        cliDirectory = cwd / 'cli'
        guiDirectory = cwd / 'gui'
        logicDirectory = cwd / 'logic'
        dataDirectory = cwd / 'data'
    
    if os.path.exists (cliDirectory):
        print ("   ...CLI directory located.")
    else: 
        print ("   ...CLI directory not found.")
        missingDirectories.append("CLI")
    if os.path.exists (guiDirectory):
        print ("   ...GUI directory located.")
    else: 
        print ("   ...GUI directory not found.")
        missingDirectories.append("GUI")
    if os.path.exists (logicDirectory):
        print ("   ...logic directory located.")
    else: 
        print ("   ...logic directory not found.")
        missingDirectories.append("Logic")
    if os.path.exists (dataDirectory):
        print ("   ...data directory located.")
    else: 
        print ("   ...data directory not found.")
        missingDirectories.append("Data")

    if os.path.exists (cliDirectory) == False or os.path.exists (guiDirectory) == False or os.path.exists (logicDirectory) == False or os.path.exists (dataDirectory) == False:
        print (f"I can't find following directories: {missingDirectories}.")
        print ()
        if os.path.exists (guiDirectory) == False:
            printw ("The GUI directory is missing, but this program can run perfectly fine from the command-line interface (CLI). User input specifying alternate locations for the UI directory is not supported at this time, but will be added in future versions soon(TM). For now, though, you're stuck with the CLI.")
            print()
            print ("If you would like to exit the program now, enter X or 0.")
            menuChoice = input ("Otherwise, press any key to continue setup. ")
            if menuChoice == '0' or menuChoice == 'X' or menuChoice == "x":
                sys.exit(0)
            else:
                pass
        else:
            printw ("This is a problem - this program will not run properly without a logic or data directory. User input specifying alternate locations for these directories is not supported at this time, but will be added in future versions soon(TM).")
            input ("Press any key to quit.")
            sys.exit(1)
    else:
        print ("All directories present.")
    print("Main setup complete.")
    print()

def MainMenu(): # Contains logic and display instructions for the main menu.
    print ()
    print (10 * "-", "Rosevomit.py Main Menu", 10 * "-" )
    print ("What sorts of names would you like to generate?")
    print ("     1. First names")
    print ("     2. First names, female-only")
    print ("     3. First names, male-only")
    print ("     4. Last names")
    print ("     5. Full names")
    print ("     6. Full names, female-only")
    print ("     7. Full names, male-only")
    print ("     8. Generate from sample data (dev purposes)")
    print ("X or 0. Exit program")
    print ()
    menuChoice = input ("Enter your choice: ")
    print ()

    if menuChoice == "1":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("first", int(_input))
    elif menuChoice == "2":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("firstfemale", int(_input))
    elif menuChoice == "3":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("firstmale", int(_input))
    elif menuChoice == "4":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("last", int(_input))
    elif menuChoice == "5":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("full", int(_input))
    elif menuChoice == "6":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("fullfemale", int(_input))
    elif menuChoice == "7":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("fullmale", int(_input))
    elif menuChoice == "8":
        _input = input ("How many first names should be generated? ")
        LogicController.gen("sample", int(_input))
    elif menuChoice == '0' or menuChoice == 'X' or menuChoice == "x":
        sys.exit(0)
    else:
        print ("Look, I'm just a computer program. I've got all the time to waste in the world, and I don't get bored. You can keep entering invalid inputs, or you can actually follow instructions. Your call.")






# *** MAIN PROGRAM STARTS HERE ***

RosevomitSetup()
print ("Proceeding to get local modules... ", end="")
CWD_home()
from logic import LogicController
from cli import TextStuff
print ("done.")

print ()
print (69 * "-")
print (27 * "-", "ROSEVOMIT.PY", 28 * "-")
print (69 * "-")
print ()

# After setup, rosevomit.py will display the main menu and will carry out instructions based on user input. This is an infinite loop - if rosevomit.py ever has no more instructions to carry out, it displays the main menu again and awaits further instructions. This is based on the 'see_rosa_run' variable. This variable should never change. If it does, the program exits and gives the system an error code.
see_rosa_run = True
while see_rosa_run is True:
    MainMenu()
else:
    sys.exit(1)
