# ----------------------------------------
# DialogExit.py
# (rosevomit/core/cli/DialogExit.py)
# ----------------------------------------
# A UI module for Alex's "Project Rosevomit" that contains the dialog for exiting the program. Prompts the user about cleanup functuons.
import re
import sys
import textwrap

from logic import TempFiles


### SOME LISTS OF REGEX PATTERNS FOR PARSING USER INPT
regexes_yes = [
    re.compile("^[Y][ES]*$", flags=re.IGNORECASE),
]
regexes_no = [
    re.compile("^[N][O]*$", flags=re.IGNORECASE),
]
# Dear future self,
# Yeah, I just learned about regular expressions. 
# You got a problem with that?
#   Love, Your(past)self
regexes_opt = [
    re.compile("^[G][IME]*$", flags=re.IGNORECASE),
    re.compile("^[M][ORE]*", flags=re.IGNORECASE),
    re.compile("^[O][PTIONS]*", flags=re.IGNORECASE),
    re.compile("^[G][IME]*\s*[M][ORE]*\s*[O][PTIONS]*$", flags=re.IGNORECASE),
]


### SOME HELPER FUNCTIONS...
def exit_menu():
    print ("-" * 16, "Exit Menu", "-" * 17)
    print ("Would you like to exit Rosevomit?")
    print ("        [Y]es (or 'enter')")
    print ("        [N]o")
    print ("        Gimme more [o]ptions")


def exit_prompt():
    _input = input ("Enter your choice, or leave blank to exit: ")
    _input = _input.strip()  # Strips all leading or trailing whitespaces
    return _input


def exit_options_menu():
    print ("EXIT MENU OPTIONS:")
    print ("     1. Exit (normal)")
    print ("     2. Exit (without cleaning temp directory)")
    print (textwrap.fill ("     3. Uh, view this program's '/temp' directory, then show me this menu again...", width=70, subsequent_indent="        "))
    print ("     4. Back to main menu")


def exit_options_prompt():
    _input = input ("Enter your option choice, or leave blank to exit: ")
    _input = _input.strip()  # Strips all leading or trailing whitespaces
    return _input


def cleanup_and_exit():
    TempFiles.delete()
    sys.exit(0)


### ...AND THE BIG MAIN FUNCTION
def exit(headless=False):
    assert type(headless) is bool
    if headless is False:
        exit_menu()
    else:
        pass

    _input = exit_prompt()
    if _input is None or _input is "" or _input is "Y" or any(re.match(pattern, _input) for pattern in regexes_yes):
        cleanup_and_exit()
    elif _input is "N" or _input is any(re.match(pattern, _input) for pattern in regexes_no):
        pass  # Ends the exit() function without doing anything
    elif _input is "o" or any(re.match(pattern, _input) for pattern in regexes_opt):
        exit_options_menu()
        _input = exit_options_prompt()
        if _input is "1":
            cleanup_and_exit()
        elif _input is "2":
            sys.exit(0)
        elif _input is "3":
            TempFiles.view()
        elif _input is "4":
            return
        else:
            print (textwrap.fill (f"Sorry, {_input} isn't a recognized command here.", width=70))
            print()
            exit(headless=False)  # Return to main exit menu, displayed fully
    else:
        print (textwrap.fill (f"Sorry, {_input} isn't a recognized command here.", width=70))
        print()
        exit(headless=True)  # Return to main exit menu without displaying the full menu options
