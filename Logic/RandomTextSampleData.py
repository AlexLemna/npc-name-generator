# ----------------------------------------
# Gets random text from /Data/simple_data/sample.txt
# ----------------------------------------

import os
import pathlib
import random
import sys

# NAVIGATES TO PROPER DIRECTORY
os.chdir (os.path.dirname (sys.argv[0])) # <-- from https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
  # Setting working directory to home folder.
os.chdir (..)
os.chdir (os.path.relpath ( '\SimpleData' ))

# Defining empty list. Explicit variable declaration isn't necessary in Python, but I like it.
contents = []

# target files is at "F:\OneDrive\CODE\Projects\npc-name-generator\Data\simple data\sample.txt"
with open('sample.txt', 'r') as fileData:
    contents = fileData.readlines()

# print ( random.choice(contents) )
