import datetime
import os
import pathlib
import sys
import textwrap
import time
import traceback

# Rosevomit test modules
import testmain
import testmiscstuff

if __name__ != "__main__":
    print (textwrap.fill ("YOU ARE TRYING TO RUN 'RunTests.py' AS A MODULE, AND YOU DIDN'T PROGRAM THIS FILE TO RUN THAT WAY! IT MAY NOT WORK PROPERLY. IF YOU MEANT TO DO THIS, THEN GO TO 'RunTests.py' AND REMOVE THIS WARNING AFTER YOU'VE LOOKED THE FILE OVER TO MAKE SURE IT WON'T START CREATING FILES IN STRANGE PLACES, ETC."))
    input()
    sys.exit(1)

AVAILABLE_TESTS = ["sanity test", "performance test", "pylint test"]
tests_to_run: list = testmiscstuff.choose_prompt (AVAILABLE_TESTS)
if len(tests_to_run) == 0:
    print ("No tests selected. Exiting now.")
    sys.exit()

# Make sure our working directory is the /devtest directory (which this file should be in)
starting_directory = pathlib.Path.cwd()
if starting_directory.name == "devtests":
    pass
else:
    try:
        os.chdir("devtests")
    except FileNotFoundError as e:  # 'FileNotFoundError' works on directories, too
        print(e)
        traceback.format_exc()
        input ("Press enter to quit.")
        sys.exit()
# Setting some constants that will be used in report headers, filenames, titles, etc.
PROJECT_NAME = "Rosevomit"
DATETIME = datetime.datetime.now()
DATESTRING = DATETIME.strftime("%Y-%b-%d (%a) %I:%M%p")
DATESTRING_SHORT = DATETIME.strftime("%Y%b%d-%H%M")
# Creating a 'testlog' directory (TESTLOG_DIR) where we'll store the test results
testlogname = str(DATESTRING_SHORT + "-test")
testlogname = testmiscstuff.make_name_unique (testlogname)
os.mkdir (testlogname)
os.chdir (testlogname)
TESTLOG_DIR = pathlib.Path.cwd()

# Moving through filesystem, looking for important directories and saving their paths as constants. Note that, as written, this program basically just looks for the directories in their expected location and freaks out if they're not there.
os.chdir ("..")
if testmiscstuff.get_cwd_name_only() == "devtests":  # NOTE: We use '==' here, not 'is'!
    DEVTEST_DIR = pathlib.Path.cwd()
else:
    raise FileNotFoundError
os.chdir ("..")
if testmiscstuff.get_cwd_name_only() == "rosevomitrepo":
    REPO_DIR = pathlib.Path.cwd()
else:
    raise FileNotFoundError
# From here, we check the main rosevomit sub-modules all together.
ROSEVOMIT_DIR = REPO_DIR / "rosevomit"
CLI_DIR = ROSEVOMIT_DIR / "programcli"
LOGIC_DIR = ROSEVOMIT_DIR / "programlogic"
DATA_DIR = ROSEVOMIT_DIR / "programdata"
TEMP_DIR = ROSEVOMIT_DIR / "temp"
directories = [ROSEVOMIT_DIR, CLI_DIR, LOGIC_DIR, DATA_DIR, TEMP_DIR]
directories_present = []
directories_missing = []
for item in directories:
    try:
        assert pathlib.Path.exists(item)
        directories_present.append(item)
    except AssertionError:
        directories_missing.append(item)

# ---------------------TESTING BEGINS---------------------
t0 = time.perf_counter()
# Running sanity test, performance test, and saving output to file
if "sanity test" in tests_to_run:
    testmain.sanity (ARG_test_directory=TESTLOG_DIR, ARG_datestring=DATESTRING, ARG_short_datestring=DATESTRING_SHORT, ARG_project=PROJECT_NAME)

# Running performance tests...
if "performance test" in tests_to_run:
    perftest10_results, perftest100_results, perftest1000_results = testmain.performance (ARG_test_directory=TESTLOG_DIR, ARG_datestring=DATESTRING, ARG_short_datestring=DATESTRING_SHORT, ARG_project=PROJECT_NAME)
else:
    perftest10_results = {}
    perftest100_results = {}
    perftest1000_results = {}

# Generating summary file
t1 = time.perf_counter()
time_elapsed = t1 - t0
testmain.summary (ARG_test_directory=TESTLOG_DIR, ARG_datestring=DATESTRING, ARG_short_datestring=DATESTRING_SHORT, ARG_project=PROJECT_NAME, ARG_directories_present=directories_present, ARG_directories_missing=directories_missing, ARG_time=time_elapsed, ARG_perfresults_10=perftest10_results, ARG_perfresults_100=perftest100_results, ARG_perfresults_1000=perftest1000_results)

# Running pylint tests...
if "pylint test" in tests_to_run:
    testmain.pylint (ARG_test_directory=TESTLOG_DIR, ARG_repository_directory=REPO_DIR, ARG_datestring=DATESTRING, ARG_short_datestring=DATESTRING_SHORT, ARG_project=PROJECT_NAME)
    # TODO: The script seems to unexpectedly end here.

print ()
print ("Testing complete. One or more text files with the test results have")
print ("been placed in:")
print ("  ", TESTLOG_DIR)
print ()
