print ("Starting LogicController.")
import pathlib
import os
import random
import runpy
import sys
import tempfile
print ("Successfully imported modules.")
print ()

print ("Checking current directory...")
with pathlib.Path.cwd() as cdpath:
    print (f"...the current directory is {cdpath}. ")
print ()

print ("Scanning current directory...")
with os.scandir() as entries:
    for entry in entries:
        print(f"   {entry.name}")
print ()

print ("Creating a temporary file and writing some data to it...")
with tempfile.TemporaryFile("w+t") as tp:
    tp.write("Hello universe!")
    tp.seek(0) # <-- Moves program back to beginning of temporary file, in preperation for reading.
    print (f"{tp.read()}")
    tp.close() # <-- Closes temporary file. It is automatically erased.
print ()

print ("Looking for UI, Logic, and Data directories...")
os.chdir ("..") # <-- Moves up to parent directory.
os.chdir ("..") # <-- ...twice.
with pathlib.Path.cwd() as cdpath: # <-- Restates 'cdpath' since it will otherwise still reflect the old directory.
    print (f"...in {cdpath}...")
    uiDirectory = cdpath / 'UI'
    logicDirectory = cdpath / 'Logic'
    dataDirectory = cdpath / 'Data'

if os.path.exists (uiDirectory):
    print ("   ...UI directory located.")
else: 
    print ("   ...UI directory not found.")
if os.path.exists (logicDirectory):
    print ("   ...logic directory located.")
else: 
    print ("   ...logic directory not found.")
if os.path.exists (dataDirectory):
    print ("   ...data directory located.")
else: 
    print ("   ...data directory not found.")
print ()

if os.path.exists (uiDirectory) == False or os.path.exists (logicDirectory) == False or os.path.exists (dataDirectory) == False:
    print("This is a problem.")
else:
    print ("Everything fine here, carry on.")

print("How are you?")