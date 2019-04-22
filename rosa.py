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
print ("done.")

# MODULES FROM PYPI (the Python community)
# none

# MY MODULES
print ("Getting some local modules... ", end="")
# from Logic import LogicController
print ("done.")

# SOME FUNCTIONS AND VARIABLES FOR EASY REFERENCE
def MainMenu():
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
    elif menuChoice == '0' or menuChoice == 'X' or menuChoice == "x":
        see_rosa_run is False
    else:
        print ("Look, I'm just a computer program. I've got all the time to waste in the world, and I don't get bored. You can keep entering invalid inputs, or you can actually follow instructions. Your call.")

# *** MAIN PROGRAM STARTS HERE ***
see_rosa_run = True
if see_rosa_run is True:
    MainMenu()
else:
    sys.exit(0)
