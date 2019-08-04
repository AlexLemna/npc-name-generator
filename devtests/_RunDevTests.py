import datetime
import io
import os
import pathlib
import subprocess
import sys
import textwrap
import traceback
import unittest

# Rosevomit test modules
import TestFunctions
import TestMiscStuff
# Rosevomit itself
from context import rosevomit

if __name__ != "__main__":
    print (textwrap.fill ("YOU ARE TRYING TO RUN 'RunTests.py' AS A MODULE, AND YOU DIDN'T PROGRAM THIS FILE TO RUN THAT WAY! IT MAY NOT WORK PROPERLY. IF YOU MEANT TO DO THIS, THEN GO TO 'RunTests.py' AND REMOVE THIS WARNING AFTER YOU'VE LOOKED THE FILE OVER TO MAKE SURE IT WON'T START CREATING FILES IN STRANGE PLACES, ETC."))
    input()
    sys.exit(1)

# Prompt the user before running tests
# (in the future, we'll ask which tests to run)
do_we_run = TestMiscStuff.run_prompt()
if do_we_run is False:
    sys.exit()
# TODO: Add ability to pick and choose which tests to run

# Make sure our working directory is the /devtest directory (which this file should be in)
starting_directory = pathlib.Path.cwd()
if starting_directory.name == "devtests":
    pass
else:
    try:
        os.chdir("devtests")
    except FileNotFoundError as e:  # 'FileNotFoundError' works on directories, too
        print(e)
        traceback.format_exc
        input ("Press enter to quit.")
        sys.exit()
# Setting some constants that will be used in report headers, filenames, titles, etc.
PROJECT_NAME = "Rosevomit"
DATETIME = datetime.datetime.now()
DATESTRING = DATETIME.strftime("%Y-%b-%d (%a) %I:%M%p")
# Creating a directory (TESTLOG_DIR) where we'll store the test results
testlogname = str("testlog-" + DATETIME.strftime("%Y%b%d-%H%M"))
testlogname = TestMiscStuff.make_name_unique (testlogname)
os.mkdir (testlogname)
os.chdir (testlogname)
TESTLOG_DIR = pathlib.Path.cwd()

# Moving through filesystem, looking for important directories and saving their paths as constants. Note that, as written, this program basically just looks for the directories in their expected location and freaks out if they're not there.
os.chdir ("..")
if TestMiscStuff.get_cwd_name_only() == "devtests":  # NOTE: We use '==' here, not 'is'!
    DEVTEST_DIR = pathlib.Path.cwd()
else:
    raise FileNotFoundError
os.chdir ("..")
if TestMiscStuff.get_cwd_name_only() == "rosevomitrepo":
    REPO_DIR = pathlib.Path.cwd()
else:
    raise FileNotFoundError
# From here, we check the main rosevomit sub-modules all together.
ROSEVOMIT_DIR = REPO_DIR / "rosevomit"
CLI_DIR = ROSEVOMIT_DIR / "programcli"
LOGIC_DIR = ROSEVOMIT_DIR / "programlogic"
DATA_DIR = ROSEVOMIT_DIR / "programdata"
TEMP_DIR = ROSEVOMIT_DIR / "temp"
for item in [ROSEVOMIT_DIR, CLI_DIR, LOGIC_DIR, DATA_DIR, TEMP_DIR]:
    assert pathlib.Path.exists(item)

# Running test and saving output to file
os.chdir (TESTLOG_DIR)
with open(testlogname + ".results.txt", "w+") as f:
    # Save original stdout and stderr settings
    _old_stdout = sys.stdout
    _old_stderr = sys.stderr
    # Switch stdout and stderr to file output
    sys.stdout = f
    sys.stderr = f
    testsuite = unittest.TestLoader().loadTestsFromModule(TestFunctions)
    unittest.TextTestRunner().run(testsuite)
    # Restore stdout and stderr to original settings
    sys.stderr = _old_stderr
    sys.stdout = _old_stdout


input("Done. Press 'enter' to escape.")
