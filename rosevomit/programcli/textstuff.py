# teststuff.py
# rosevomit.programcli.teststuff
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
