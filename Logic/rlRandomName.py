# ----------------------------------------
# rlRandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosa" that contains functions for randomly generating names.

import os
import random
import sys

# Defining empty list. Explicit variable declaration isn't necessary in Python, but I like it.
contents = []

def CWD_home(): # Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
    os.chdir (os.path.dirname (sys.argv[0]))

# target files is at \Data\SampleData.txt"
def SampleData ():
  if __name__ == "__main__": # Checks if this program is running as the main script (only hallens for debugging purposes)
    CWD_home()
    os.chdir ("..")
    os.chdir ( ".\Data" )
    with open('SampleData.txt', 'r') as fileData:
      contents = fileData.readlines()
      print ( random.choice(contents) )
  elif __name__ == "Logic.rlRandomName": # This is the normal module behavior - it's being run from somewhere else.
    CWD_home()
    os.chdir ( ".\Data" )
    with open('SampleData.txt', 'r') as fileData:
      contents = fileData.readlines()
      return ( random.choice(contents) )
  else: # I'm honestly not sure what situation wouldn't fit into the two statements above. If that happens, though, I want to pause the program and take a look!
    import pdb
    pdb.set_trace() # Creates a breakpoint.

SampleData()
# print ( f"{SampleData}" )
