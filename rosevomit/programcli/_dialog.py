# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# worsecli.py
# rosevomit.programcli.worsecli
# ___________________________________________________________________
"""A file containing the base functions for a command line interface dialog."""
from distutils.util import strtobool
import re

from core import REGEXES_NO, REGEXES_YES
from programcli import formatting, messages

# ---------- Prompts ----------
def _prompt_hint_bool (ARG_default: bool) -> str:
    """Determines which prompt hint to show the user."""
    if ARG_default is True:
        return "([Yes]/No)"
    elif ARG_default is False:
        return "([Yes]/No)"
    else:
        # ARG_default must be bool.
        raise TypeError


def prompt_generic (ARG_prompt: str) -> str:
    """Displays a prompt, accepts input, cleans it, and returns it."""
    _input = formatting.inputwrap (ARG_prompt)
    result = _input.strip()
    if result == "":
        messages.unrecognized_input_message (result)
        recursive_result = prompt_generic (ARG_prompt)
        result = recursive_result
    return result


def prompt_yesno (ARG_prompt: str, ARG_default: bool=True) -> bool:
    """Asks the user a yes/no question, and returns the result as a bool."""
    prompt = ARG_prompt.strip()
    input_hint = _prompt_hint_bool (ARG_default)
    _input = formatting.inputwrap (f"{prompt} {input_hint}")
    _input = _input.strip()

    if _input == "":
        return ARG_default
    elif any (re.match (pattern, _input) for pattern in REGEXES_YES):
        return True
    elif any (re.match (pattern, _input) for pattern in REGEXES_NO):
        return False
    else:
        messages.unrecognized_input_message (_input)
        recursive_result = prompt_yesno (ARG_prompt)
        return recursive_result

# ---------- Menus ----------
def _menu_from_options(ARG_menuoptions, ARG_returns_to: str):
    """Displays a menu from a list or tuple of options. Unlike a menu from a dict (see '_menu_from_keyed_options()'), this menu will have automatically assigned 'keys'. The 'ARG_returns_to' is the 'parent' menu, and is always offered as the '0' option."""
    assert isinstance (ARG_menuoptions, (list, tuple))
    formatting.printwrap (f"0. {ARG_returns_to}", ARG_indented=True)
    for option_number, option in enumerate (ARG_menuoptions):
        formatting.printwrap (f"{option_number}. {option}", ARG_indented=True)


def _menu_from_keyed_options (ARG_menuoptions: dict, ARG_returns_to: str):
    """NOT YET IMPLEMENTED!"""
    raise NotImplementedError("The developer has not yet implemented menus based on dicts yet!")


def menu(ARG_name: str, ARG_parent_menu_name: str, ARG_options):
    """Displays a menu of options. Technically, a wrapper function for a bunch of other internal functions that it calls depending on the type of ARG_options."""
    formatting.menu_title (ARG_name)
    if isinstance (ARG_options, (list, tuple)):
        _menu_from_options (ARG_options, ARG_returns_to=ARG_parent_menu_name)
    elif isinstance (ARG_options, dict):
        _menu_from_keyed_options (ARG_options, ARG_returns_to=ARG_parent_menu_name)
    else:
        raise TypeError

# ---------- Displays ----------
def display_directory_contents():
    """Displays the contents of a directory."""
    raise NotImplementedError
