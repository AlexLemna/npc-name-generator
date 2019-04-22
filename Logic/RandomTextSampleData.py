# ----------------------------------------
# Gets random text from /Data/simple_data/sample.txt
# ----------------------------------------

import os
import pathlib
import random
import sys

# Defining empty list. Explicit variable declaration isn't necessary in Python, but I like it.
contents = []

# target files is at "F:\OneDrive\CODE\Projects\npc-name-generator\Data\simple data\sample.txt"
def fRandomTextSampleData ():
  os.chdir (os.path.dirname (sys.argv[0])) # <-- Sets working directory to home folder. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
  os.chdir ("..")
  os.chdir ( ".\Data\SimpleData" )
  with open('sample.txt', 'r') as fileData:
    contents = fileData.readlines()
    return ( random.choice(contents) )
  
fRandomTextSampleData()

# ------------------------------------
# RANDOM SNIPPETS FOR DEBUGGING:
#
# with pathlib.Path.cwd() as cwd:
#   print (f"My cwd is {cwd}.")
