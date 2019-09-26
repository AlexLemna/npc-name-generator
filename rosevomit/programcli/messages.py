# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# messages.py
# rosevomit.programcli.messages
# ___________________________________________________________________
"""Contains system messages to display to users."""
from programcli import textstuff


def general_program_message (ARG_string: str):
    """Displays a textwrapped message, and then 'Press Enter to Continue.' The user can then press enter."""
    print ()
    textstuff.printwrap (f"{ARG_string} Press 'Enter' to continue.")
    input()


def warning_version_is_prerelease (ARG_major_version, ARG_minor_version, ARG_patch_version):
    """Displays a warning that this version is pre-release version."""
    textstuff.printwrap (f"You are using Rosevomit version {ARG_major_version}.{ARG_minor_version}.{ARG_patch_version}. This software is actively under development. Proceed at your own risk.")


def warning_version_is_devbuild ():
    """Displays a warning that this version is a development build for a version past 1.0. For prerelease devbuilds, use 'warning_version_is_prerelease_devbuild()'.

    NOT CURRENTLY USED.
    """
    # Will be written once we hit version 1.0
    raise NotImplementedError


def warning_version_is_prerelease_devbuild (ARG_major_version, ARG_minor_version, ARG_patch_version):
    """Displays a warning that this version is both a pre-release version and a development build."""
    textstuff.printwrap (f"You are using a development build of Rosevomit {ARG_major_version}.{ARG_minor_version}.{ARG_patch_version}. This software is actively under development, and this development build may not be stable! Proceed at your own risk.")
