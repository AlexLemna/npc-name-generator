# teststuff.py
# rosevomit.programcli.teststuff
# ___________________________________________________________________
"""A file containing functions used for the formatting of output messages."""
import textwrap


def printwrap(x, indented=False, end_with='\n'):
    """Textwrapping for regular 'print' commands."""
    if indented is True:
        print (textwrap.fill (x, width=70, subsequent_indent="   "), end=end_with)
    else:
        print (textwrap.fill (x, width=70), end=end_with)


def inputwrap(x, indented=False, end_with=" "):
    """Textwrapping for regular 'input' commands."""
    if indented is True:
        _input = input (textwrap.fill (x, width=70, subsequent_indent="   ") + end_with)
        return _input
    else:
        _input = input (textwrap.fill (x, width=70) + end_with)
        return _input
