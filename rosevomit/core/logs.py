# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# logs.py
# rosevomit.core.logs
# ___________________________________________________________________
"""This file contains config dictionaries for the default logger."""
import logging

# See https://docs.python.org/3/howto/logging-cookbook.html
# create parent logger
mainlogger = logging.getLogger("logger")
mainlogger.setLevel (logging.DEBUG)
# create file handler which logs even debug messages
filehandler1 = logging.FileHandler("logdata/debug.log")
filehandler1.setLevel (logging.DEBUG)
filehandler2 = logging.FileHandler("logdata/info.log")
filehandler2.setLevel (logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter ("%(asctime)s at %(filename)s: line %(lineno)d - %(name)s - %(levelname)s - %(message)s")
filehandler1.setFormatter (formatter)
filehandler2.setFormatter (formatter)
# add the handler to the logger
mainlogger.addHandler (filehandler1)
mainlogger.addHandler (filehandler2)


class BaseLogger:  # pylint: disable=too-few-public-methods
    """Auxiliary logger, which can be called from other modules."""
    def __init__(self, ARG_loggername: str):
        self.logger = logging.getLogger (f"logger.{ARG_loggername}")
