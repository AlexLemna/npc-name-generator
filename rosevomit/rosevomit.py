# --------------------
# ROSEVOMIT.PY
# --------------------
# The main file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python.

print ()
print ("Starting ROSEVOMIT.")
# MODULES FROM PYTHON'S STANDARD LIBRARY
print ("Getting some modules from the standard library... ", end="")
import os
import sys
print ("done.")
# INTERNAL MODULES
print ("Proceeding to get local modules... ", end="")
from core import settings, startup
from programcli import dialogexit, worsecli
print ("done.")


# SOME FUNCTIONS
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
        worsecli.submenu_name_show()
        worsecli.submenu_name_input()
        show_main_menu()
    elif menuchoice == "2":
        worsecli.submenu_timeline_show()
        worsecli.submenu_timeline_input()
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


# **********************************************
# ********** MAIN PROGRAM STARTS HERE **********
# **********************************************
HOME_DIRECTORY = os.path.dirname (sys.argv[0])

if settings.existence() is False:
    print ("The settings don't exist. Recreating settings file at:")
    print (f"  {settings.SETTINGS_FILE}")
    settings.restore_file()
    print ()
else:
    pass
startup.main_setup(HOME_DIRECTORY)

print ()
print (69 * "-")
print (27 * "-", "ROSEVOMIT.PY", 28 * "-")
print (69 * "-")
print ()

# After setup, rosevomit.py will display the main menu and will carry out instructions based on user input. This is an infinite loop - if rosevomit.py ever has no more instructions to carry out, it displays the main menu again and awaits further instructions. This is based on the 'see_rosa_run' variable. This variable should never change. If it does, the program exits and gives the system an error code.
see_rosa_run = True
show_main_menu()
while see_rosa_run is True:
    ask_for_input()
else:
    sys.exit(1)
