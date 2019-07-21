# ----------------------------------------
# WorseCLI.py
# ----------------------------------------
# A UI module for Alex's "Project Rosevomit" that contains functions for displaying menus beyond Rosevomits's main menu, and for processing the inputs for those menus.

from logic import LogicController


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
        _input = input ("How many first names should be generated? ")
        print ()
        LogicController.gen("first", int(_input))
        print ()
    elif menuchoice == "2":
        _input = input ("How many female first names should be generated? ")
        print ()
        LogicController.gen("firstfemale", int(_input))
        print ()
    elif menuchoice == "3":
        _input = input ("How many male first names should be generated? ")
        print ()
        LogicController.gen("firstmale", int(_input))
        print ()
    elif menuchoice == "4":
        _input = input ("How many last names should be generated? ")
        print ()
        LogicController.gen("last", int(_input))
        print ()
    elif menuchoice == "5":
        _input = input ("How many full names should be generated? ")
        print ()
        LogicController.gen("full", int(_input))
        print ()
    elif menuchoice == "6":
        _input = input ("How many female full names should be generated? ")
        print ()
        LogicController.gen("fullfemale", int(_input))
        print ()
    elif menuchoice == "7":
        _input = input ("How many male full names should be generated? ")
        print ()
        LogicController.gen("fullmale", int(_input))
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
        _input = input ("How many years of historical global events should be generated? ")
        print ()
        LogicController.gen("globalevents", int(_input))
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
        print()
        submenu_timeline_input()
