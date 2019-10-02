# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# dialogexit.py
# rosevomit.programcli.dialogexit
# ___________________________________________________________________
"""A UI module that contains the dialog for exiting the program."""
import sys

from programcli import _dialog


def simple_exit_dialog():
    """This function displays a message asking the user to confirm the program exit."""
    print ()
    do_we_exit: bool = _dialog.prompt_yesno (ARG_prompt="Are you sure you want to exit?")
    if do_we_exit is True:
        sys.exit(0)
