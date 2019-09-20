# pylint: disable=global-statement

import configparser
import os
import textwrap

# ---------- Contents ----------
# ---------- -------- ----------
# This module has four subsections:
#   1. "Meta" functions (for handling the settings-data.ini file itself)
#   2. Functions for reading settings
#   3. Helper functions for displaying the settings dialog (used by the function in section 5)
#   4. The main function for displaying the settings dialog to the user

# This is an "always relative to this module" filepath
SETTINGS_FILE = os.path.join (os.path.dirname (__file__), "settings-data.ini")

# ---------- (1) "META" FUNCTIONS ----------
# These functions deal with the actual existence of the settings-data.ini file, and the recreation of it if necessary.
def existence() -> bool:
    """Checks to see if the file defined as the global constant SETTINGS_FILE exists.

    Note: this function might have trouble locating the SETTINGS_FILE if run as a module.
    """
    _result = os.path.isfile(SETTINGS_FILE)
    return _result


def is_valid() -> bool:
    """Checks to see if the file specified as the 'SETTINGS_FILE' has certain expected options and values."""
    try:
        startup_dialog()
        logging_service()
        exit_dialog()
    except configparser.Error:
        return False
    else:
        return True


def restore_file():
    """Recreates the file specified in the 'SETTINGS_FILE' variable using internally defined defaults."""
    # Initializing ConfigParser()
    config = configparser.ConfigParser()
    # Entering the default values we want to restore
    config["debugging"] = {
        "startup_dialog": "on",
        "logging_service": "off"}
    config["directories"] = {}
    config["exit behavior"] = {"exit_dialog": "on"}
    # Creating the file
    with open(SETTINGS_FILE, "w+") as newfile:
        # Writing header comment
        newfile.write("; ROSEVOMIT/CORE/SETTINGS/SETTINGS.INI\n")
        newfile.write("; a file storing Rosevomit's settings\n")
        newfile.write("\n")
        # Writing default values
        config.write(newfile)

# ---------- (2) FUNCTIONS FOR READING SETTINGS ----------
# These functions are used for reading the values of settings from the settings file, either for display to the user or for internal program use.
# For developer readibility, these functions should be listed below in the same order that the values they read in the settings-data.ini file are listed.
def startup_dialog() -> bool:
    """Returns true or false based on the value of startup_dialog' in the 'settings-data.ini' file."""
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean(section="debugging", option="startup_dialog")
    return result


def logging_service() -> bool:
    """Returns true of false based on the value of 'logging_service' in the 'settings-data.ini' file."""
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean(section="debugging", option="logging_service")
    return result


def exit_dialog() -> bool:
    """Returns true or false based on the value of 'exit dialog' in the 'settings-data.ini' file."""
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean(section="exit behavior", option="exit_dialog")
    return result

# ---------- (3) HELPER FUNCTIONS FOR DISPLAYING SETTINGS DIALOG ----------
def prompt_to_change_settings() -> bool:
    """Asks the user if they want to change any settings. Returns true if the user enters 'y' and false if the user enters nothing or 'n'."""
    _input = input ("Would you like to change any settings? y/[n]: ")
    _input = _input.strip()
    if _input == "n" or _input == "":
        return False
    elif _input == "y":
        return True
    else:
        print (f"Sorry, {_input} is not a valid option. Please enter 'y' or 'n'.")
        recursive_response = prompt_to_change_settings()
        return recursive_response


def _prompt_for_section_name (ARG_config_object) -> str:
    """Prompts the user to enter a valid section name. Checks that section name exists."""
    print ()
    print ("Type the section name of the setting you would like to change, or")
    _input = input ("leave blank to exit: ")
    _input = _input.strip()
    if _input == "":
        return
    section_name = _input.lower()
    if ARG_config_object.has_section (section_name) is False:
        print (f"Sorry, {section_name} is not a valid section name.")
        recursive_result = _prompt_for_section_name (ARG_config_object)
        return recursive_result
    else:
        return section_name


def _prompt_for_option_name (ARG_config_object, ARG_section: str) -> str:
    """Prompts the user to enter a valid option name. Checks that option name exists."""
    print ()
    print (f"SELECTED SECTION: {ARG_section}")
    print ("Type the option name of the setting you would like to change, or")
    _input = input ("leave blank to exit: ")
    _input = _input.strip()
    if _input == "":
        return
    option_name = _input.lower()
    if ARG_config_object.has_option (ARG_section, option_name) is False:
        print (f"Sorry, {option_name} is not a valid option name.")
        recursive_result = _prompt_for_option_name(ARG_config_object , ARG_section)
        return recursive_result
    else:
        return option_name


def _prompt_for_new_value (ARG_section: str, ARG_option: str) -> str:
    """Prompts the user to enter a new value.
    
    Unlike the other '_prompt_ functions, we don't need an argument for the ConfigParser object becasuse we aren't using using any of its validation methods."""
    print ()
    print (f"SELECTED SECTION: {ARG_section}, SELECTED OPTION: {ARG_option}")
    _input = input ("Type the desired new value, or leave blank to exit: ")
    _input = _input.strip()
    if _input == "":
        return
    else:
        new_value = _input
        return new_value



def dialog_change_setting():
    """Asks the user to type the name of the setting they wish to change. Validates that the user's input is an actual name ('key') in the 'settings-data.ini' file. Launches the appropriate function to change that setting."""
    global SETTINGS_FILE
    settings = open (SETTINGS_FILE)
    config = configparser.ConfigParser()
    config.read_file(settings)

    section: str = _prompt_for_section_name (config)
    if section is None:
        return
    option: str = _prompt_for_option_name (config, section)
    if option is None:
        return
    value: str = _prompt_for_new_value (section, option)
    if value is None:
        return
    config.set (section, option, value)
    settings = open (SETTINGS_FILE, "w")
    config.write (settings)
    print (f"Option {option} in section {section} was set to {value}")
    print()


# ---------- (4) MAIN FUNCTION FOR DISPLAYING SETTINGS DIALOG ----------
# NOTE: Perhaps this should go in the programcli folder? Need to think about it.
def settings_user_interface (header: bool=True):
    """Displays a command-line interface to the user for viewing and/or modifying current settings."""
    print ()
    if header:
        print (10 * "-", "Settings", 10 * "-")
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()
    config.read_file(settings)

    settings_sections: list = config.sections()
    if len (settings_sections) < 1:
        print (textwrap.fill ("WARNING: The setting file appears to be blank. Please close Rosevomit and restart it - Rosevomit should detect a corrupted settings file and offer to restore the settings file to its default state."))
        input ()
        return
    else:
        print ("The current settings are listed below in the format")
        print ("  'SECTION'")
        print ("    'OPTION': 'VALUE'")
        print ()
        for section in settings_sections:
            print ()
            print (f"  {section}")
            options = config.items (section)
            if len (options) >= 1:
                for item in options:
                    key = item[0]
                    value = item[1]
                    print (f"    {key}: {value}")
            else:
                print (f"    (no options in this section)")
    print ()

    do_we_change_settings: bool = prompt_to_change_settings()
    if do_we_change_settings is True:
        dialog_change_setting ()
        settings_user_interface (header=False)
    elif do_we_change_settings is False:
        return  # return to whatever menu/function called this function
    else:
        # TODO: RealityError candidate?
        raise TypeError
