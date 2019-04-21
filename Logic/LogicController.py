print ()
print ("Starting LogicController. Importing modules... ", end = "")
import pathlib
import os
import runpy
import sys
import tempfile
print ("done. ", end="")

print ("Setting my home folder as the current working directory... ", end="")
os.chdir(os.path.dirname(sys.argv[0])) # <-- from https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
print ("done. ")

with pathlib.Path.cwd() as homepath:
    print (f"   My home folder is {homepath}.")
print ()

os.chdir ("..") # <-- Moves up to parent directory.
print ("Looking for UI, Logic, and Data directories in my parent folder...")
with pathlib.Path.cwd() as parentPath:
    uiDirectory = parentPath / 'UI'
    logicDirectory = parentPath / 'Logic'
    dataDirectory = parentPath / 'Data'

missingDirectories = []
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
    print (f"   (Parent folder is {parentPath})")
    print("I'm currently missing the following directories:", end="")
    print("",missingDirectories, end=". ")
    print("This is a problem.")
else:
    print ("Everything fine here, carry on.")
print()

print ("Random output from local text file: ", end="")
runpy.run_module ('RandomFromFile')

print("How are you?")