# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# tempfiles.py
# rosevomit.core.tempfiles
# ___________________________________________________________________
"""A logic module that handles files in the /temp directory."""
import os
import pathlib
import shutil
import textwrap

from core.constants import TEMP_DIRECTORY_PATH


def _check_that_cwd_is_temp():
    """Checks to see if we are in the temp directory."""
    with pathlib.Path.cwd() as cwd:
        p = pathlib.PurePath (cwd)
        if p.parts[-1] != "temp":
            print ("POSSIBLE ERROR:")
            print (textwrap.fill ("We should have found Rosevomit's /temp firectory, but we seem to have gotten lost instead."))
            print ("CURRENT LOCATION:")
            print (cwd)
            print ()
            input ("Press any key to continue.")
            raise FileNotFoundError


def is_empty() -> bool:
    """Checks to see if the /temp directory is empty. Returns a bool."""
    os.chdir (TEMP_DIRECTORY_PATH)
    _check_that_cwd_is_temp()
    with pathlib.Path.cwd() as cwd:
        number_of_items_in_directory = len (os.listdir (cwd))
    if number_of_items_in_directory == 0:
        result = True
    elif number_of_items_in_directory > 0:
        result = False
    else:
        # TODO: Reality error candidate?
        raise ValueError ("'number_of_items_in_directory' cannot be negative.")
    return result


def delete():
    """Clears out the temp directory."""
    os.chdir (TEMP_DIRECTORY_PATH)
    _check_that_cwd_is_temp()
    with pathlib.Path.cwd() as cwd:
        for filename in os.listdir(cwd):
            filepath = os.path.join(cwd, filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)


def view():
    """Prints a list of the contents of the temp directory."""
    os.chdir (TEMP_DIRECTORY_PATH)
    _check_that_cwd_is_temp()
    with pathlib.Path.cwd() as cwd:
        num_of_items = len (os.listdir (cwd))
        print (f"{num_of_items} temporary items currently exist...")
        for filename in os.listdir(cwd):
            print (f"    {filename}")
        print ()


def save(ARG_file, ARG_overwrite: bool=False, ARG_dialog: bool=True):
    """Copies a file from the temp directory to the saved directory."""
    os.chdir (TEMP_DIRECTORY_PATH)
    _check_that_cwd_is_temp()
    with pathlib.Path.cwd() as cwd:
        if ARG_file not in os.listdir(cwd):
            raise FileNotFoundError
        elif os.path.exists(f"..\\saved\\{ARG_file}") and ARG_overwrite is False:
            raise FileExistsError
    shutil.copy2( ARG_file, '..\\saved')
    if ARG_dialog is True:
        print (f"...{ARG_file} saved.")
