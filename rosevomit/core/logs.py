# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# logs.py
# rosevomit.core.logs
# ___________________________________________________________________
"""This file contains config dictionaries for the default logger."""
import logging
import logging.handlers
import os


class BaseLogger:  # pylint: disable=too-few-public-methods
    """Auxiliary logger, which can be called from other modules."""
    def __init__(self, ARG_loggername: str):
        self.logger = logging.getLogger (f"{ARG_loggername}")
        self.logger.info ("Logger initialized.")

_LOGALOG = BaseLogger(__name__)

from core.constants import LOG_DIRECTORY_PATH

def _startsession (ARG_targetfile):
    """Writes a blank line and a session header to the targetfile."""
    with open(ARG_targetfile, "a") as f:
        f.write("\n---------- BEGIN SESSION ----------\n")


def start_logging(ARG_parentlogger, ARG_bufferlogger):
    """Create file handlers, creates formatter and adds it to the handlers, and adds those handlers to logger."""
    filehandlers = []

    debugfile = os.path.join (LOG_DIRECTORY_PATH, "10-debug.log")
    _startsession (debugfile)
    filehandler1 = logging.FileHandler(debugfile)
    filehandler1.setLevel (logging.DEBUG)
    filehandlers.append (filehandler1)

    infofile = os.path.join (LOG_DIRECTORY_PATH, "20-info.log")
    _startsession (infofile)
    filehandler2 = logging.FileHandler(infofile)
    filehandler2.setLevel (logging.INFO)
    filehandlers.append (filehandler2)

    warnfile = os.path.join (LOG_DIRECTORY_PATH, "30-warning.log")
    _startsession (warnfile)
    filehandler3 = logging.FileHandler(warnfile)
    filehandler3.setLevel (logging.WARNING)
    filehandlers.append (filehandler3)

    errorfile = os.path.join (LOG_DIRECTORY_PATH, "40-error.log")
    _startsession (errorfile)
    filehandler4 = logging.FileHandler(errorfile)
    filehandler4.setLevel (logging.ERROR)
    filehandlers.append (filehandler4)

    criticalfile = os.path.join (LOG_DIRECTORY_PATH, "50-critical.log")
    _startsession (criticalfile)
    filehandler5 = logging.FileHandler(criticalfile)
    filehandler5.setLevel (logging.CRITICAL)
    filehandlers.append (filehandler5)

    formatter = logging.Formatter ("%(asctime)s %(name)s @ %(filename)s:%(lineno)d - %(levelname)s - %(funcName)s: %(message)s")
    for item in filehandlers:
        item.setFormatter (formatter)
        ARG_parentlogger.addHandler (item)

    bufferfile = os.path.join (LOG_DIRECTORY_PATH, "00-buffer.log")
    _startsession (bufferfile)
    bufferfilehandler = logging.FileHandler(bufferfile)
    bufferfilehandler.setFormatter(formatter)

    ARG_bufferlogger.setTarget(bufferfilehandler)
    ARG_bufferlogger.flush()
    ARG_bufferlogger.close()
