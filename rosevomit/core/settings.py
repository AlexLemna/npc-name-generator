import configparser
import os

# This is an "always relative to this module" filepath
SETTINGS_FILE = os.path.join (os.path.dirname (__file__), "settings-data.ini")


def existence() -> bool:
    """Checks to see if the file defined as the global constant SETTINGS_FILE exists.

    Note: this function might have trouble locating the SETTINGS_FILE if run as a module.
    """
    _result = os.path.isfile(SETTINGS_FILE)
    return _result


def restore_file():
    """Recreates the file specified in the 'SETTINGS_FILE' variable  using internally defined defaults."""
    check_existence: bool = existence()
    if check_existence is True:
        raise FileExistsError
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
        # Header comment
        newfile.write("; ROSEVOMIT/CORE/SETTINGS/SETTINGS.INI\n")
        newfile.write("; a file storing Rosevomit's settings\n")
        newfile.write("\n")
        # Writing default values
        config.write(newfile)


def dialog_on_exit() -> bool:
    """Returns true or false based on the value of 'exit dialog' in the 'settings-data.ini' file."""
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Created an instance of ConfigParser
    config.read_file(settings)
    _result: bool = config.getboolean(section="exit behavior", option="exit_dialog")
    return _result


def debug_startup() -> bool:
    """Returns true or false based on the value of startup_dialog' in the 'settings-data.ini' file."""
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Created an instance of ConfigParser
    config.read_file(settings)
    _result: bool = config.getboolean(section="debugging", option="startup_dialog")
    return _result
