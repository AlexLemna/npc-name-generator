# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# tempfiles.py
# rosevomit.core.tempfiles
# ___________________________________________________________________
"""A logic module that handles files in the /temp directory."""
import os
import pathlib
import shutil
import sys
import textwrap


def delete():
    """Clears out the temp directory."""
    os.chdir (sys.path[0])
    os.chdir ("./temp")
    with pathlib.Path.cwd() as cwd:
        p = pathlib.PurePath (cwd)
        if p.parts[-1] != "temp":
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
    """Prints a list of the contents of the temp directory."""
    os.chdir (sys.path[0])
    os.chdir ("./temp")
    with pathlib.Path.cwd() as cwd:
        p = pathlib.PurePath (cwd)
        if p.parts[-1] != "temp":
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

def save(ARG_file, ARG_overwrite: bool=False, ARG_dialog: bool=True):
    """Copies a file from the temp directory to the saved directory."""
    os.chdir (sys.path[0])
    os.chdir ("./temp")
    with pathlib.Path.cwd() as cwd:
        p = pathlib.PurePath (cwd)
        if p.parts[-1] != "temp":
            print ("POSSIBLE ERROR:")
            print (textwrap.fill ("We should have found Rosevomit's /temp firectory, but we seem to have gotten lost instead."))
            print ("CURRENT LOCATION:")
            print (cwd)
            print ()
            input ("Press any key to continue.")
        elif ARG_file not in os.listdir(cwd):
            raise FileNotFoundError
        else:
            if os.path.exists(f"..\\saved\\{ARG_file}") and ARG_overwrite is False:
                raise FileExistsError
            shutil.copy2( ARG_file, '..\\saved')
            if ARG_dialog is True:
                print (f"...{ARG_file} saved.")
