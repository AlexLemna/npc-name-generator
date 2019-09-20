import datetime

from testmain import FINDIMPORTS_MODULE_EXISTS, PYLINT_MODULE_EXISTS

# Setting some constants that will be used in report headers, filenames, titles, etc.
PROJECT_NAME = "Rosevomit"
current_time = datetime.datetime.now()
DATESTRING = current_time.strftime ("%Y-%b-%d (%a) %I:%M%p")
DATESTRING_SHORT = current_time.strftime ("%Y%b%d-%H%M")

FINDIMPORTS_AVAILABLE: bool = FINDIMPORTS_MODULE_EXISTS
PYLINT_AVAILABLE: bool = PYLINT_MODULE_EXISTS
