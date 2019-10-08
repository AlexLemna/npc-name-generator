# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# logs.py
# rosevomit.core.logs
# ___________________________________________________________________
"""This file contains config dictionaries for the default logger."""
import logging
import os

from core.constants import LOG_DIRECTORY_PATH


# See https://docs.python.org/3/howto/logging-cookbook.html
# create parent logger
parentlogger = logging.getLogger("")
parentlogger.setLevel (logging.DEBUG)

# create file handler which logs even debug messages
debugfile = os.path.join (LOG_DIRECTORY_PATH, "10-debug.log")
with open(debugfile, "a") as f:
    f.write("\n---------- BEGIN SESSION ----------\n")
filehandler1 = logging.FileHandler(debugfile)
filehandler1.setLevel (logging.DEBUG)

infofile = os.path.join (LOG_DIRECTORY_PATH, "20-info.log")
with open(infofile, "a") as f:
    f.write("\n---------- BEGIN SESSION ----------\n")
filehandler2 = logging.FileHandler(infofile)
filehandler2.setLevel (logging.INFO)

warnfile = os.path.join (LOG_DIRECTORY_PATH, "30-warning.log")
with open(warnfile, "a") as f:
    f.write("\n---------- BEGIN SESSION ----------\n")
filehandler3 = logging.FileHandler(warnfile)
filehandler3.setLevel (logging.WARNING)

errorfile = os.path.join (LOG_DIRECTORY_PATH, "40-error.log")
with open(errorfile, "a") as f:
    f.write("\n---------- BEGIN SESSION ----------\n")
filehandler4 = logging.FileHandler(errorfile)
filehandler4.setLevel (logging.ERROR)

criticalfile = os.path.join (LOG_DIRECTORY_PATH, "50-critical.log")
with open(criticalfile, "a") as f:
    f.write("\n---------- BEGIN SESSION ----------\n")
filehandler5 = logging.FileHandler(criticalfile)
filehandler5.setLevel (logging.CRITICAL)

# create formatter and add it to the handlers
formatter = logging.Formatter ("%(asctime)s %(name)s @ %(filename)s:%(lineno)d - %(levelname)s - %(funcName)s: %(message)s")
filehandler1.setFormatter (formatter)
filehandler2.setFormatter (formatter)
filehandler3.setFormatter (formatter)
filehandler4.setFormatter (formatter)
filehandler5.setFormatter (formatter)

# add the handler to the logger
parentlogger.addHandler (filehandler1)
parentlogger.addHandler (filehandler2)
parentlogger.addHandler (filehandler3)
parentlogger.addHandler (filehandler4)
parentlogger.addHandler (filehandler5)


class BaseLogger:  # pylint: disable=too-few-public-methods
    """Auxiliary logger, which can be called from other modules."""
    def __init__(self, ARG_loggername: str):
        self.logger = logging.getLogger (f"{ARG_loggername}")
        self.logger.info ("Logger initialized.")
