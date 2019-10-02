# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# formatting.py
# rosevomit.programcli.formatting
# ___________________________________________________________________
"""A file containing functions used for the formatting of output messages."""
import textwrap


def printwrap(x, ARG_indented: bool=False, ARG_end_with: str='\n'):
    """Textwrapping for regular 'print' commands."""
    if ARG_indented is True:
        print (textwrap.fill (x, width=70, subsequent_indent="   "), end=ARG_end_with)
    else:
        print (textwrap.fill (x, width=70), end=ARG_end_with)


def inputwrap(x, ARG_indented: bool=False, ARG_end_with: str=" "):
    """Textwrapping for regular 'input' commands."""
    if ARG_indented is True:
        _input = input (textwrap.fill (x, width=70, subsequent_indent="   ") + ARG_end_with)
        return _input
    else:
        _input = input (textwrap.fill (x, width=70) + ARG_end_with)
        return _input

# ---------- Menu titles ----------
def _menutitlestring (ARG_title: str) -> str:
    """Returns a suitable title string that is uppercase, and ends in 'MENU', and is less than or equal to 70 characters long."""
    title = str (ARG_title)  # If ARG_title isn't a string, we definitely want it to be
    if len (title) > 65:
        title = title[0:64]  # Cuts off anything beyond 65 characters (standard width of an old terminal window is 70 characters, and we're potentially adding 5 characters below)
    title = title.strip()
    title = title.upper()
    last_5_characters = title[-5:]  # We want our menu title to end in "MENU"
    if last_5_characters != " MENU":
        title = title + " MENU"
    return title


def menu_title (ARG_menuname: str):
    """Standardized formatting for a menu title. Prints an empty line, then prints a menu title."""
    print()
    titlestring = _menutitlestring (ARG_menuname)
    print (titlestring)
