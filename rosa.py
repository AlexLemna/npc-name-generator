# --------------------
# ROSA.PY
# --------------------
# The main file for Alex's "Project Rosa", a random name generator written in Python.

print ()
print (70 * "-")
print (30 * "-", "ROSA.PY", 31 * "-")
print (70 * "-")
print ()

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

# MY MODULES
def myModules():
    print ("Getting some local modules... ")
    from Logic import LogicController
    LogicController.setup()
    print ("Local modules imported.")

# SOME FUNCTIONS AND VARIABLES FOR EASY REFERENCE
def CWD_home(): # Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
    os.chdir (os.path.dirname (sys.argv[0]))

def printw(x): # Textwrapping for regular 'print' commands.
    print ( textwrap.fill (x, width = 70))

def inputw(x): # Textwrapping for user input prompts.
    input ( textwrap.fill (x, width=70))

def RosaSetup(): # Contains setup instructions.
    print ("Looking for UI, Logic, and Data directories...")
    missingDirectories = []
    CWD_home ()
    with pathlib.Path.cwd() as cwd:
        uiDirectory = cwd / 'UI'
        logicDirectory = cwd / 'Logic'
        dataDirectory = cwd / 'Data'
    
    if os.path.exists (uiDirectory):
        print ("   ...UI directory located.")
    else: 
        print ("   ...UI directory not found.")
        missingDirectories.append("UI")
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

    if os.path.exists (uiDirectory) == False or os.path.exists (logicDirectory) == False or os.path.exists (dataDirectory) == False:
        print (f"I can't find following directories: {missingDirectories}.")
        print ()
        if os.path.exists (uiDirectory) == False:
            printw ("The UI directory is missing, but this program can run perfectly fine from the command-line interface (CLI). User input specifying alternate locations for the UI directory is not supported at this time, but will be added in future versions soon(TM). For now, though, you're stuck with the CLI.")
            print()
            menuChoice = inputw ("If you would like to exit the program now, enter X or 0. Otherwise, press any key to continue setup. ")
            if menuChoice == '0' or menuChoice == 'X' or menuChoice == "x":
                sys.exit(0) # Exits the program. "0" is the exit code for a successful program exiting. "1" is the exit code for a program exiting due to an error.
            else:
                pass
        else:
            printw ("This is a problem - this program will not run properly without a logic or data directory. User input specifying alternate locations for these directories is not supported at this time, but will be added in future versions soon(TM).")
            input ("Press any key to quit.")
            sys.exit(1) # Exits the program. "0" is the exit code for a successful program exiting. "1" is the exit code for a program exiting due to an error.
    else:
        print ("All directories present. Proceeding to get local modules.")
    print("Setup complete.")
    print()



def MainMenu(): # Contains logic and display instructions for the main menu.
    print ()
    print (10 * "-", "Rosa.py Main Menu", 10 * "-" )
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
        pass
    elif menuChoice == "2":
        pass
    elif menuChoice == "3":
        pass
    elif menuChoice == "4":
        pass
    elif menuChoice == "5":
        pass
    elif menuChoice == "6":
        pass
    elif menuChoice == "7":
        pass
    elif menuChoice == "8":
        LogicController.gen("sample")
    elif menuChoice == '0' or menuChoice == 'X' or menuChoice == "x":
        see_rosa_run is False
    else:
        print ("Look, I'm just a computer program. I've got all the time to waste in the world, and I don't get bored. You can keep entering invalid inputs, or you can actually follow instructions. Your call.")

# *** MAIN PROGRAM STARTS HERE ***
RosaSetup()
from Logic import LogicController

see_rosa_run = True
if see_rosa_run is True:
    MainMenu()
else:
    sys.exit(0)
