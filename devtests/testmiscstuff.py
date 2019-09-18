import os
import pathlib
import sys
import traceback


def choose_prompt(ARG_choicelist: list):
    tests_to_run: list = []
    print ("Would you like to (y) run all tests (default), or (n) select")
    _input = input ("specific tests? Enter 'y' or 'n': ")
    _input = _input.strip()
    if _input == "y" or _input == "":
        tests_to_run = ARG_choicelist
        return tests_to_run
    elif _input == "n":
        tests_to_run = choose_tests (tests_to_run, ARG_choicelist)
        return tests_to_run
    else:
        print ("Sorry, please enter either 'y' or 'n'.")
        choose_prompt(ARG_choicelist)


def choose_tests(ARG_selectionlist: list, ARG_choicelist: list) -> list:
    print (f"The selected tests are: {ARG_selectionlist}")
    print (f"The available tests are:")
    num = 0
    for item in ARG_choicelist:
        num = num + 1
        print (f"  {num}. {item}")
    print ("Type a number to add that test to the list of selected tests, or")
    _input = input ("leave blank to run the currently selected tests: ")
    _input = _input.strip()
    if _input == "":
        return ARG_selectionlist
    else:
        try:
            _selection_num = int (_input)
        except TypeError:
            print (f"{_input} is not a valid input. Please try again.")
            choose_tests (ARG_selectionlist, ARG_choicelist)
        if _selection_num <= len(ARG_choicelist):
            _selection_num = _selection_num - 1  # list indexing starts at 0
            selectionlist = ARG_selectionlist
            selectionlist.append (ARG_choicelist[_selection_num])
            selections = choose_tests (selectionlist, ARG_choicelist)
            return selections
        else:
            print (f"{_selection_num} is not a valid input. Please try again.")
            choose_tests (ARG_selectionlist, ARG_choicelist)


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


# THANKS: https://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto/40054132#40054132
class Suppressor(object):

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self

    def __exit__(self, type, value, traceback):
        sys.stdout = self.stdout
        if type is not None:
            # Do normal exception handling
            raise

    def write(self, x):
        pass
