import os
import pathlib


def run_prompt():
    _input = input ("Would you like to run some tests? ([y]/n) ")
    if _input == "y" or _input == "":
        return True
    elif _input == "n":
        return False
    else:
        print ("Sorry, please enter either 'y' or 'n'.")
        run_prompt()


def make_name_unique (basename: str) -> str:
    """If the basename isn't unique within the current working directory, this function adds an integer to the end of the basename and increments it until it becomes unique."""
    number = 1
    name = basename
    while os.path.exists (name) is True:
        number = number + 1
        name = basename + "-" + str(number)
        pass
    return name


def get_cwd_name_only():
    """Returns only the folder name of the current working directory, not the full path."""
    _cwd = pathlib.Path.cwd()
    _path_split = os.path.split(_cwd)
    return _path_split[-1]


def logformat_line(char: str = "_", newline: bool = False) -> None:
    """Prints a character 70 times, with an optional preceding newline."""
    if newline is True:
        print ()
    if len(char) is 1:
        print (char * 70)
    else:
        raise ValueError  # TODO: Custom exception?


def logformat_header(text: str) -> None:
    """Prints a centered, all-uppercase header for the unittest log files. Tries to center the 'headertext' for a 70-character column width. """
    if not str.isupper(text):
        text = str.upper(text)
    num_spaces = int ((70 - len (text)) / 2)
    print (" " * num_spaces, text, " " * num_spaces, sep="")
