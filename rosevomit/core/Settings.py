import configparser
import os

# This is an "always relative to this module" filepath
SETTINGS_FILE = os.path.join (os.path.dirname (__file__), "settings-data.ini")


def existence():
    """Checks to see if the file defined as the global constant SETTINGS_FILE exists.

    Note: this function might have trouble locating the SETTINGS_FILE if run as a module.
    """
    _result = os.path.isfile(SETTINGS_FILE)
    return _result


def restore_file():
    """Recreates the file specified in the 'SETTINGS_FILE' variable  using internally defined defaults."""
    if check_existence is True:
        raise FileExistsError
    # Initializing ConfigParser()
    settings = configparser.ConfigParser()
    # Entering the default values we want to restore
    settings["debugging"] = {
        "startup_dialog": "on",
        "logging_service": "off"}
    settings["directories"] = {}
    settings["exit behavior"] = {"exit_dialog": "on"}
    # Creating the file
    with open(SETTINGS_FILE, "w+") as newfile:
        # Header comment
        newfile.write("; ROSEVOMIT/CORE/SETTINGS/SETTINGS.INI\n")
        newfile.write("; a file storing Rosevomit's settings\n")
        newfile.write("\n")
        # Writing default values
        settings.write(newfile)
