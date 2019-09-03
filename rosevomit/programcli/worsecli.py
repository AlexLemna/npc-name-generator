# ----------------------------------------
# WorseCLI.py
# ----------------------------------------
# A UI module for Alex's "Project Rosevomit" that contains functions for displaying menus beyond Rosevomits's main menu, and for processing the inputs for those menus.
import re
import sys

from . import dialogexit
from core import settings
from programlogic import logiccontroller


def input_integer(_prompt_text="", _if_invalid=None):
    """Prompts the user for an integer, and checks to make sure that the user's input is actually an integer. If it is, it returns the integer. If it is not, it informs the user of the invalid input and prompts them again for valid input or runs the function passed to it through the '_if_invalid' argument."""
    _prompt = _prompt_text.rstrip()  # Strips whitespaces at tne end.
    if _prompt is "" or _prompt is None:
        _input = input ("Please enter a positive integer: ")
    else:
        _input = input (f"{_prompt} ")
    _input = _input.rstrip()  # Strips whitespaces at the end.
    try:
        _input = abs (int (_input))
        return _input
    except ValueError:
        print ("Sorry, that's not a valid number.")
        if _if_invalid is "" or _if_invalid is None:
            input_integer(_prompt)
        else:
            _if_invalid()


def submenu_name_show():
    """Contains display instructions for the name generation menu."""
    print ()
    print ("What sorts of names would you like to generate?")
    print ("     1. First names")
    print ("     2. First names, female-only")
    print ("     3. First names, male-only")
    print ("     4. Last names")
    print ("     5. Full names")
    print ("     6. Full names, female-only")
    print ("     7. Full names, male-only")
    print ("     0. Back to main menu.")
    print ("     X. Exit program")
    print ()


def submenu_name_input():
    """Asks for user input and processes it. Contains logic for the name generation submenu."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if menuchoice == "1":
        _input = input_integer ("How many first names should be generated? ")
        print ()
        logiccontroller.gen("first", int(_input))
        print ()
    elif menuchoice == "2":
        _input = input_integer ("How many female first names should be generated? ")
        print ()
        logiccontroller.gen("firstfemale", int(_input))
        print ()
    elif menuchoice == "3":
        _input = input_integer ("How many male first names should be generated? ")
        print ()
        logiccontroller.gen("firstmale", int(_input))
        print ()
    elif menuchoice == "4":
        _input = input_integer ("How many last names should be generated? ")
        print ()
        logiccontroller.gen("last", int(_input))
        print ()
    elif menuchoice == "5":
        _input = input_integer ("How many full names should be generated? ")
        print ()
        logiccontroller.gen("full", int(_input))
        print ()
    elif menuchoice == "6":
        _input = input_integer ("How many female full names should be generated? ")
        print ()
        logiccontroller.gen("fullfemale", int(_input))
        print ()
    elif menuchoice == "7":
        _input = input_integer ("How many male full names should be generated? ")
        print ()
        logiccontroller.gen("fullmale", int(_input))
        print ()
    elif menuchoice == '0':
        pass
    elif menuchoice == 'X' or menuchoice == "x" or menuchoice == "exit":
        sys.exit(0)
    elif menuchoice == "help" or menuchoice == "'help'" or menuchoice == "h" or menuchoice == "H" or menuchoice == "helf":
        submenu_name_show()
        submenu_name_input()
    elif menuchoice == "":
        submenu_name_input()
    else:
        print (f"{menuchoice} is not a recognized command.")
        print()
        submenu_name_input()


def submenu_timeline_show():
    """Contains display instructions for the timeline generation menu."""
    print ()
    print ("What sort of timeline would you like to generate?")
    print ("     1. Global events")
    print ("     2. Regional events (NOT CURRENTLY SUPPORTED)")
    print ("     0. Back to main menu.")
    print ("     X. Exit program")
    print ()


def submenu_timeline_input():
    """Asks for user input and processes it. Contains logic for the name generation submenu."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if menuchoice == "1":
        _input = input_integer ("How many years of historical global events should be generated? ")
        print ()
        logiccontroller.gen_timeline("globalevents", int(_input))
        print ()
    elif menuchoice == "2":
        print ("This option is not currently supported.")
        submenu_timeline_input ()
    elif menuchoice == '0':
        pass
    elif menuchoice == 'X' or menuchoice == "x" or menuchoice == "exit":
        sys.exit(0)
    elif menuchoice == "help" or menuchoice == "'help'" or menuchoice == "h" or menuchoice == "H" or menuchoice == "helf":
        submenu_timeline_show()
        submenu_timeline_input()
    elif menuchoice == "":
        submenu_timeline_input()
    else:
        print (f"{menuchoice} is not a recognized command.")
        submenu_timeline_input()


def prompt_save():
    """Asks the user if they want to save, and processes response."""
    menuchoice = input ("Would you like to save this result? (Yes/No) ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if re.search(r"^[y][es]*$", menuchoice, flags=re.IGNORECASE):
        return True
    elif re.search(r"^[n][o]*$", menuchoice, flags=re.IGNORECASE):
        return False
    else:
        print (f"{menuchoice} is not a recognized command.")
        prompt_save()


def show_main_menu():
    """Contains display instructions for the main menu."""
    print ()
    print (10 * "-", "Rosevomit.py Main Menu", 10 * "-")
    print ("What would you like to generate?")
    print ("     1. Random names")
    print ("     2. A random timeline")
    print ("X or 0. Exit program")
    print ()


def ask_for_input():
    """Asks for user input and processes it. Contains logic for the main menu."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if menuchoice == "1":
        submenu_name_show()
        submenu_name_input()
        show_main_menu()
    elif menuchoice == "2":
        submenu_timeline_show()
        submenu_timeline_input()
        show_main_menu()
    elif menuchoice == '0' or menuchoice == 'X' or menuchoice == "x" or menuchoice == "exit":
        show_exit_dialog = settings.dialog_on_exit()
        if show_exit_dialog is False:
            sys.exit()
        else:
            do_we_exit = dialogexit.exit()  # dialogexit.exit() should either return False or close the program itself
            if do_we_exit is False:
                show_main_menu()
    elif menuchoice == "help" or menuchoice == "'help'" or menuchoice == "h" or menuchoice == "H" or menuchoice == "helf":
        show_main_menu()
    elif menuchoice == "":
        ask_for_input()
    else:
        print (f"{menuchoice} is not a recognized command.")