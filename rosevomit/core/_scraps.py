"""This file just contains some scraps that I'm not using now, but want to keep for reference in the future. This is a temporary file - I may delete it without warning, so DO NOT call from it!"""
# These imports are just here so I can get the relevant tooltips in VSCode, this does NOT indicate that this is a usable module!
from pathlib import Path

from core.constants import LOG_DIRECTORY_PATH

# --- Dictionaries with the config information for the loggers ---
# See https://docs.python.org/3/howto/logging-cookbook.html#an-example-dictionary-based-configuration and https://docs.python.org/3/library/logging.config.html#logging-config-fileformat
LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s at %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(funcName)s: %(message)s"}
    },
    "handlers": {
        "debug": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "default",
            "filename": Path(LOG_DIRECTORY_PATH).joinpath("debug.log"),
        },
        "info": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "default",
            "filename": Path(LOG_DIRECTORY_PATH).joinpath("info.log"),
        },
        "warning": {
            "class": "logging.FileHandler",
            "level": "WARNING",
            "formatter": "default",
            "filename": Path(LOG_DIRECTORY_PATH).joinpath("warning.log"),
        },
        "error": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "default",
            "filename": Path(LOG_DIRECTORY_PATH).joinpath("error.log"),
        },
        "critical": {
            "class": "logging.FileHandler",
            "level": "CRITICAL",
            "formatter": "default",
            "filename": Path(LOG_DIRECTORY_PATH).joinpath("critical.log"),
        },
    },
    "loggers": {
        "debug": {
            "handlers": ["debug"],
            "level": "DEBUG",
        },
        "info": {
            "handlers": ["debug", "info"],
            "level": "INFO",
        },
        "warning": {
            "handlers": ["debug", "info", "warning"],
            "level": "WARNING",
        },
        "error": {
            "handlers": ["debug", "info", "warning", "error"],
            "level": "ERROR",
        },
        "critical": {
            "handlers": ["debug", "info", "warning", "error", "critical"],
            "level": "CRITICAL",
        },
    },
}

# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# _static_constants.py
# rosevomit.core._static_constants
# ___________________________________________________________________
"""This file contains the program's static constants. These are kept in a separate module from the dynamic constants partially for organizational purposes, but also to avoid 'import loops' that might occur if the dynamic constants were kept in the same file as the static constants that some of the dynamic constants use to define themselves."""
_CORE_DIRECTORY_NAME = "core"
LOG_DIRECTORY_NAME = "core/logdata"
CLI_DIRECTORY_NAME = "programcli"
LOGIC_DIRECTORY_NAME = "programlogic"
DATA_DIRECTORY_NAME = "programdata"
TEMP_DIRECTORY_NAME = "temp"
SAVE_DIRECTORY_NAME = "saved"
