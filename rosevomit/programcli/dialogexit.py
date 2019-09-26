# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# dialogexit.py
# rosevomit.programcli.dialogexit
# ___________________________________________________________________
"""A UI module that contains the dialog for exiting the program. Prompts the user about cleanup functions."""
import re
import sys
import textwrap

from core import tempfiles
from core.constants import REGEXES_NO, REGEXES_OPT, REGEXES_YES

### SOME HELPER FUNCTIONS...
def exit_menu():
    """Show exit menu."""
    print ("-" * 16, "Exit Menu", "-" * 17)
    print ("Would you like to exit Rosevomit?")
    print ("        [Y]es (or 'enter')")
    print ("        [N]o")
    print ("        Gimme more [o]ptions")


def exit_prompt():
    """Show exit menu prompt (suitable after exit menu)."""
    _input = input ("Enter your choice, or leave blank to exit: ")
    _input = _input.strip()  # Strips all leading or trailing whitespaces
    return _input


def exit_options_menu():
    """Show exit options menu."""
    print ("EXIT MENU OPTIONS:")
    print ("     1. Exit (normal)")
    print ("     2. Exit (without cleaning temp directory)")
    print (textwrap.fill ("     3. Uh, view this program's '/temp' directory, then show me this menu again...", width=70, subsequent_indent="        "))
    print ("     4. Back to main menu")


def exit_options_prompt():
    """Show exit options menu prompt (suitable after exit options menu)."""
    _input = input ("Enter your option choice, or leave blank to exit: ")
    _input = _input.strip()  # Strips all leading or trailing whitespaces
    return _input


def cleanup_and_exit():
    """Delete the contents of the 'temp' directory and exit."""
    tempfiles.delete()
    sys.exit(0)


### ...AND THE BIG MAIN FUNCTION
def exit_rosevomit(headless=False):
    """This function handles all calls to exit Rosevomit. It handles the logic behing displaying menus, calling appropriate functions to parse the user input, and appropriate actions to take before exit."""
    assert type(headless) is bool
    if headless is False:
        exit_menu()
    else:
        pass

    _input = exit_prompt()
    if _input is None or _input is "" or _input is "Y" or any(re.match(pattern, _input) for pattern in REGEXES_YES):
        cleanup_and_exit()
    elif _input is "N" or any(re.match(pattern, _input) for pattern in REGEXES_NO):
        return False
    elif _input is "o" or any(re.match(pattern, _input) for pattern in REGEXES_OPT):
        exit_options_menu()
        _input = exit_options_prompt()
        if _input is "1":
            cleanup_and_exit()
        elif _input is "2":
            sys.exit(0)
        elif _input is "3":
            tempfiles.view()
            exit_rosevomit(headless=False)
        elif _input is "4":
            return
        else:
            print (textwrap.fill (f"Sorry, {_input} isn't a recognized command here.", width=70))
            print()
            exit_rosevomit(headless=False)  # Return to main exit menu, displayed fully
    else:
        print (textwrap.fill (f"Sorry, {_input} isn't a recognized command here.", width=70))
        print()
        exit_rosevomit(headless=True)  # Return to main exit menu without displaying the full menu options
