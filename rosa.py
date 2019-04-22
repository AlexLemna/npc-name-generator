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

os.chdir(os.path.dirname(sys.argv[0]))
print (sys.path)


# MY MODULES
print ("Getting some local modules... ", end="")
import RandomTextSampleData
print ("done.")

# SOME FUNCTIONS AND VARIABLES FOR EASY REFERENCE

# *** MAIN PROGRAM STARTS HERE ***
