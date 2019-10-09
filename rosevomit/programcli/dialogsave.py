# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# dialogsave.py
# rosevomit.programcli.dialogsave
# ___________________________________________________________________
"""A UI module that contains the dialog for saving files."""
import typing

import core.utilities as ut
from core import logs, tempfiles
from programcli import _dialog, formatting, messages

_SAVE_DIALOG_LOGGER = logs.BaseLogger (__name__)


def prompt_save_yesno (ARG_filename: str="") -> bool:
    """Asks the user if they want to save ARG_file. Basically a convenient wrapper around prompt_yesno()."""
    if ARG_filename == "":
        result = _dialog.prompt_yesno ("Do you want to save the results? ")
    else:
        result = _dialog.prompt_yesno (f"Save {ARG_filename}? ")
    return result


def prompt_savename (ARG_format: str) -> str:
    """Asks the user what name they want to save the file under."""
    if ARG_format[0] != ".":
        extension = "." + ARG_format
    else:
        extension = ARG_format
    prompt = f"Save the {extension} file as: "
    filename = _dialog.prompt_generic (prompt)
    result = filename + extension
    return result


def proactive(ARG_defaultname: str="file"):
    """Use this function *before* generating data.
    Returns:
      savebool: A True/False value. If True, the data should be saved at /saved/'filename'. If False, the data should be saved at /temp/'filename'.
      filename: A string.
    """
    savebool: bool
    filename: str

    savebool = _dialog.prompt_yesno ("Do you want to save the data once it is generated? (If you choose not to save the data right now, it still may be available in the /temp directory later. No guarentees, though.)")

    # TODO: Move "setname" from here to suncalc.main
    _default_name = ut.setname(ARG_defaultname)
    assert isinstance (savebool, bool)
    if savebool is True:
        _input = formatting.inputwrap (f"Do you want to save this file as {_default_name}? Leave blank to accept this name, or enter a name of your choice. You don't need to enter the file extension: ")
        _input = _input.strip()  # Strips all leading or trailing whitespaces
        filename = f"{_input}"
    else:
        filename = _default_name
    return savebool, filename


# TODO: break the following function in to two functions - one where the user can decide if the exiting file should be overwritten, and one to prompt the user for a new name.
def filealreadyexists(ARG_filename) -> typing.Union[str, bool]:
    """Use this function when the user tries to save data using a name that already exists.
    Returns:
      (either)
      save_as: A string that can be used as the new filename to save data under.
      (or)
      True: This function returns true if the user decides to keep the original file and delete the current data without saving it.
      False: This function returns false if the user decides to overwrite the original file with the new data.
    """
    formatting.printwrap (f"A file with the filename 'saved/{ARG_filename}' already exists. What should we do with the temporary file 'temp/{ARG_filename}'?")
    formatting.printwrap (f"    1. Overwrite the old 'saved/{ARG_filename}' using 'temp/{ARG_filename}'")
    formatting.printwrap (f"    2. Keep the old 'saved/{ARG_filename}' and delete 'temp/{ARG_filename}'")
    formatting.printwrap (f"    3. Save 'temp/{ARG_filename}' under a new name.")
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
        messages.unrecognized_input_message (_input)
        recursive_result = filealreadyexists(ARG_filename)
        return recursive_result
