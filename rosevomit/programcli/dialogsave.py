# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# dialogsave.py
# rosevomit.programcli.dialogsave
# ___________________________________________________________________
"""A UI module that contains the dialog for saving files."""
import os
import pathlib
import re
import typing

try:
    import textstuff
except ImportError:
    from programcli import textstuff

import core.utilities as ut
from core.constants import REGEXES_NO, REGEXES_YES
from core import tempfiles


def proactive(ARG_defaultname: str="file"):
    """Use this function *before* generating data.
    Returns:
      savebool: A True/False value. If True, the data should be saved at /saved/'filename'. If False, the data should be saved at /temp/'filename'.
      filename: A string.
    """
    savebool: bool
    filename: str

    _input = textstuff.inputwrap ("Do you want to save the data once it is generated? (If you choose not to save the data right now, it still may be available in the /temp directory later. No guarentees, though.) Enter [y]es or no. ")
    _input = _input.strip()
    if _input in (None, "", "y", "Y") or any(re.match(pattern, _input) for pattern in REGEXES_YES):
        savebool = True
    elif _input in ("N", "n") or any(re.match(pattern, _input) for pattern in REGEXES_NO):
        savebool = False
    else:
        textstuff.printwrap (f"Sorry, {_input} isn't a recognized command here.", width=70)
        print()
        proactive(ARG_defaultname)

    # TODO: Move "setname" from here to suncalc.main
    _default_name = ut.setname(ARG_defaultname)
    assert isinstance (savebool, bool)
    if savebool is True:
        _input = textstuff.inputwrap (f"Do you want to save this file as {_default_name}? Leave blank to accept this name, or enter a name of your choice. You don't need to enter the file extension: ")
        _input = _input.strip()  # Strips all leading or trailing whitespaces
        filename = f"{_input}"
    else:
        filename = _default_name
    return savebool, filename


def reactive(ARG_defaultname: str="file", ARG_fileformat: str="txt"):
    """Use this function when data has already been generated and stored in the /temp directory. It's the equivalent of a "Do you want to save your work?" prompt.
    Returns:
      files_to_save: A list of files to save. If it returns empty, save no files.
    """
    files_to_save: list = []

    tempfiles.view()
    _input = textstuff.inputwrap ("Would you like to save some/all of these files? Enter [y]es or no: ")
    _input = _input.strip()
    if _input in (None, "", "y", "Y") or any(re.match(pattern, _input) for pattern in REGEXES_YES):
        _savebool = True
    elif _input in ("N", "n") or any(re.match(pattern, _input) for pattern in REGEXES_NO):
        _savebool = False
    else:
        textstuff.printwrap (f"Sorry, {_input} isn't a recognized command here.", width=70)
        print()
        reactive(ARG_defaultname, ARG_fileformat)

    # TODO: Fix "setname" so that it checks for the file extensions during the setname function itself.
    _default_name = ut.setname(ARG_defaultname, ARG_fileformat)
    assert isinstance (_savebool, bool)
    if _savebool is False:
        return files_to_save
    else:
        with pathlib.Path.cwd() as cwd:
            p = pathlib.PurePath (cwd)
        if p.parts[-1] is not "temp":
            # TODO: Possible candidate for a custom exception? "Unexpected working directory?"
            raise FileNotFoundError
        else:
            num_of_items = len (os.listdir (cwd))
            current_item_num = 1
            for filename in os.listdir (cwd):
                print ()
                print (f"File {current_item_num} of {num_of_items}: {filename}")
                _input = input (f"Save {filename}? Enter [y]es or no: ")
                if _input in (None, "", "y", "Y") or any(re.match(pattern, _input) for pattern in REGEXES_YES):
                    files_to_save.append(filename)
                    current_item_num = current_item_num + 1
                elif _input in ("N", "n") or any(re.match(pattern, _input) for pattern in REGEXES_NO):
                    current_item_num = current_item_num + 1
                else:
                    # TODO: This is stupid. Fix this so we don't have to restart this whole thing. This may mean breaking this up into multiple functions.
                    textstuff.printwrap (f"Sorry, {_input} isn't a recognized command here.", width=70)
                    print()
                    reactive(ARG_defaultname, ARG_fileformat)
            return files_to_save


def filealreadyexists(ARG_filename) -> typing.Union[str, bool]:
    textstuff.printwrap (f"A file with the filename 'saved/{ARG_filename}' already exists. What should we do with the temporary file 'temp/{ARG_filename}'?")
    textstuff.printwrap (f"    2. Overwrite the old 'saved/{ARG_filename}' using 'temp/{ARG_filename}'")
    textstuff.printwrap (f"    1. Keep the old 'saved/{ARG_filename}' and delete 'temp/{ARG_filename}'")
    textstuff.printwrap (f"    3. Save 'temp/{ARG_filename}' under a new name.")
    _input = input ("Choose an option: ")
    _input = _input.strip()
    if _input == "1":
        return False
    elif _input == "2":
        return True
    elif _input == "3":
        save_as = input ("Enter new name: ")
        save_as = save_as.strip()
        if save_as == "":
            save_as = "new-" + ARG_filename
        return save_as
    else:
        textstuff.printwrap (f"Sorry, {_input} isn't a recognized command here.", width=70)
        print()
        filealreadyexists(ARG_filename)
