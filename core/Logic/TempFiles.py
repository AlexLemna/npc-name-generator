# ----------------------------------------
# TempFiles.py
# (rosevomit/core/logic/TempFiles.py)
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that handles files in the /temp directory.
import os
import pathlib
import shutil
import sys
import textwrap


def delete():
    os.chdir (sys.path[0])
    os.chdir ("./temp")
    with pathlib.Path.cwd() as cwd:
        p = pathlib.PurePath (cwd)
        if p.parts[-1] is not "temp":
            print ("POSSIBLE ERROR:")
            print (textwrap.fill ("We should have found Rosevomit's /temp firectory, but we seem to have gotten lost instead."))
            print ("CURRENT LOCATION:")
            print (cwd)
            print ()
            input ("Press any key to continue.")
        else:
            for filename in os.listdir(cwd):
                filepath = os.path.join(cwd, filename)
                try:
                    shutil.rmtree(filepath)
                except OSError:
                    os.remove(filepath)


def view():
    os.chdir (sys.path[0])
    os.chdir ("./temp")
    with pathlib.Path.cwd() as cwd:
        p = pathlib.PurePath (cwd)
        if p.parts[-1] is not "temp":
            print ("POSSIBLE ERROR:")
            print (textwrap.fill ("We should have found Rosevomit's /temp firectory, but we seem to have gotten lost instead."))
            print ("CURRENT LOCATION:")
            print (cwd)
            print ()
            input ("Press any key to continue.")
        else:
            num_of_items = len (os.listdir (cwd))
            print (f"{num_of_items} temporary items currently exist...")
            for filename in os.listdir(cwd):
                print (f"    {filename}")
            print ()
