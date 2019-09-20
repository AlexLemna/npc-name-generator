import os
import pathlib
import platform
import statistics
import sys
import textwrap
import time
import traceback

# Rosevomit test modules
import testmain
import testmiscstuff
from constants import DATESTRING, DATESTRING_SHORT, FINDIMPORTS_AVAILABLE, PROJECT_NAME, PYLINT_AVAILABLE

if __name__ != "__main__":
    print (textwrap.fill ("YOU ARE TRYING TO RUN 'RunTests.py' AS A MODULE, AND YOU DIDN'T PROGRAM THIS FILE TO RUN THAT WAY! IT MAY NOT WORK PROPERLY. IF YOU MEANT TO DO THIS, THEN GO TO 'RunTests.py' AND REMOVE THIS WARNING AFTER YOU'VE LOOKED THE FILE OVER TO MAKE SURE IT WON'T START CREATING FILES IN STRANGE PLACES, ETC."))
    input()
    sys.exit(1)

# ---------------------MAIN PROGRAM BEGINS---------------------
# The program begins by asking the user to determine which tests should be run.
available_tests = [
    "sanity",
    "performance",
    ]
# TODO: The section below is commented out until we can fix how the findimports module handles extended unicode characters
"""
if FINDIMPORTS_AVAILABLE is True:
    available_tests.append ("imports")
    available_tests.append ("unused imports")
"""
if PYLINT_AVAILABLE is True:
    available_tests.append ("pylint")
tests_to_run: list = testmiscstuff.choose_prompt (available_tests)
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
successful_tests = []
failed_tests = []
t0 = time.perf_counter()
print ()
# Running sanity test, performance test, and saving output to file
if "sanity" in tests_to_run:
    print ("Running sanity tests... ", end="")
    testmain.sanity (ARG_test_directory=TESTLOG_DIR)
    successful_tests.append ("sanity")
    print ("done.")

# Running performance tests...
if "performance" in tests_to_run:
    print ("Running performance tests... ", end="")
    perftest10_results, perftest100_results, perftest1000_results = testmain.performance (ARG_test_directory=TESTLOG_DIR)
    successful_tests.append ("performance")
    print ("done.")
else:
    perftest10_results = {}
    perftest100_results = {}
    perftest1000_results = {}

# Generating imports list...
if "imports" in tests_to_run:
    print ("Generating import list... ", end="")
    if FINDIMPORTS_AVAILABLE is True:
        testmain.imports (ARG_test_directory=TESTLOG_DIR, ARG_rosevomit_directory=ROSEVOMIT_DIR)
        successful_tests.append ("imports")
        print ("done.")
    elif FINDIMPORTS_AVAILABLE is False:
        failed_tests.append ("imports")
        print ("ERROR.")
        print ("The 'findimports' module is not present.")
        print ("An import list will not be generated for this test.")
    else:
        raise TypeError  # TODO: RealityError candidate

# Generating unused imports list...
if "unused imports" in tests_to_run:
    print ("Generating unused import list... ", end="")
    if FINDIMPORTS_AVAILABLE is True:
        testmain.unused_imports (ARG_test_directory=TESTLOG_DIR, ARG_rosevomit_directory=ROSEVOMIT_DIR)
        successful_tests.append ("unused imports")
        print ("done.")
    elif FINDIMPORTS_AVAILABLE is False:
        failed_tests.append ("unused imports")
        print ("ERROR.")
        print ("The 'findimports' module is not present.")
        print ("An unused import list will not be generated for this test.")
    else:
        raise TypeError  # TODO: RealityError candidate

# Running pylint tests...
if "pylint" in tests_to_run:
    print ("Running pylint... ", end="")
    if PYLINT_AVAILABLE is True:
        testmain.pylint (ARG_test_directory=TESTLOG_DIR, ARG_repository_directory=REPO_DIR)
        successful_tests.append ("pylint")
        print ("done.")
    elif PYLINT_AVAILABLE is False:
        failed_tests.append ("pylint")
        print ("ERROR.")
        print ("The 'pylint' module is not present.")
        print ("A pylint report will not be generated for this test.")
    else:
        raise TypeError  # TODO: RealityError

t1 = time.perf_counter()
time_elapsed = t1 - t0

# Generating summary file
os.chdir (TESTLOG_DIR)
print ("Writing summary file... ", end="")
with open(DATESTRING_SHORT + ".summary.txt", "w+") as f:
    # Save original stdout and stderr settings
    _old_stdout = sys.stdout
    _old_stderr = sys.stderr
    # Switch stdout and stderr to file output
    sys.stdout = f
    sys.stderr = f

    print (PROJECT_NAME, "test suite results")
    print (DATESTRING)
    testmiscstuff.logformat_line ()
    testmiscstuff.logformat_header ("ENVIRONMENT")
    print ("Python version:", platform.python_version(), platform.python_implementation())
    pybuild = platform.python_build()
    print ("  build:", pybuild[0])
    print ("        ", pybuild[1])
    print ("  compiler:", platform.python_compiler())
    print ("Python path:")
    for p in sys.path:
        print ("  ", p)

    testmiscstuff.logformat_line ()
    testmiscstuff.logformat_header ("TEST AND PROGRAM OVERVIEW")
    print ("Directories found:", len (directories_present))
    for item in directories_present:
        print ("  ", item)
    print ()
    print ("Directories not found:", len (directories_missing))
    for item in directories_missing:
        print ("  ", item)
    print ()
    if FINDIMPORTS_AVAILABLE is False:
        print (textwrap.fill ("The third-party module 'findimports' was not present, therefore the following tests were not run: import list, unused imports list"))
    display_testtime = round (time_elapsed, ndigits=1)
    # For explanations of the '//' and '%' operators, see here: https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
    display_minutes = int (time_elapsed // 60)
    display_seconds = round ((time_elapsed % 60), ndigits=1)
    print (f"Tests successfully run:", len (successful_tests))
    for item in successful_tests:
        print ("  ", item)
    print (f"Tests failed to run:", len (failed_tests))
    for item in failed_tests:
        print ("  ", item)
    print (f"Time to run tests:")
    print (f"  {display_testtime} seconds, or")
    print (f"  {display_minutes} minutes, {display_seconds} seconds")

    if "sanity" in successful_tests:
        testmiscstuff.logformat_line ()
        testmiscstuff.logformat_header ("GENERATOR SANITY TEST")
        print ("Blah blah blah.")

    if "performance" in successful_tests:
        testmiscstuff.logformat_line ()
        testmiscstuff.logformat_header ("PERFORMANCE TEST")
        print ("Blah blah blah.")
        # TODO: See below
        print (textwrap.fill ("TODO: Need to distinguish between minimum, minimum average, and real average. Or, need to find a better naming scheme."))
        print ()
        print ("Fastest performance when generating 10 names, per namelist:")
        for key, value in perftest10_results.items():
            # Also converts results from seconds to milliseconds for readibility
            minresult = min (value) * 1000
            maxresult = max (value) * 1000
            meanresult = statistics.mean (value) * 1000
            display_min = int (round (minresult, ndigits=0))
            display_min_avg = round ((minresult / 10), ndigits=2)
            display_avg = round ((meanresult / 10), ndigits=2)
            print (f"   {key}: {display_min}ms total, avg {display_min_avg}ms per name. (Real avg {display_avg}ms)")
        print ()
        print ("Fastest performance when generating 100 names, per namelist:")
        for key, value in perftest100_results.items():
            # Also converts results from seconds to milliseconds for readibility
            minresult = min (value) * 1000
            maxresult = max (value) * 1000
            meanresult = statistics.mean (value) * 1000
            display_min = int (round (minresult, ndigits=0))
            display_min_avg = round ((minresult / 100), ndigits=2)
            display_avg = round ((meanresult / 100), ndigits=2)
            print (f"   {key}: {display_min}ms total, avg {display_min_avg}ms per name. (Real avg {display_avg}ms)")
        print ()
        print ("Fastest performance when generating 1,000 names, per namelist:")
        for key, value in perftest1000_results.items():
            # Also converts results from seconds to milliseconds for readibility
            minresult = min (value) * 1000
            maxresult = max (value) * 1000
            meanresult = statistics.mean (value) * 1000
            display_min = int (round (minresult, ndigits=0))
            display_min_avg = round ((minresult / 1000), ndigits=2)
            display_avg = round ((meanresult / 1000), ndigits=2)
            print (f"   {key}: {display_min}ms total, avg {display_min_avg}ms per name. (Real avg {display_avg}ms)")

    # Restore stdout and stderr to original settings
    sys.stderr = _old_stderr
    sys.stdout = _old_stdout
print ("done.")

print ()
print ("Testing complete. One or more text files with the test results have")
print ("been placed in:")
print ("  ", TESTLOG_DIR)
print ()
