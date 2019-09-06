import datetime
import io
import os
import pathlib
import platform
import statistics
import subprocess
import sys
import textwrap
import time
import traceback
import unittest

try:
    import findimports
except ImportError:
    FINDIMPORTS_MODULE_EXISTS = False
else:
    FINDIMPORTS_MODULE_EXISTS = True

try:
    from pylint import lint as linter
except ImportError:
    PYLINT_MODULE_EXISTS = False
else:
    PYLINT_MODULE_EXISTS = True


# Rosevomit test modules
from performancetests import timetest_name_generation
import testfunctions
import testmiscstuff
# Rosevomit itself
from context import rosevomit

if __name__ != "__main__":
    print (textwrap.fill ("YOU ARE TRYING TO RUN 'RunTests.py' AS A MODULE, AND YOU DIDN'T PROGRAM THIS FILE TO RUN THAT WAY! IT MAY NOT WORK PROPERLY. IF YOU MEANT TO DO THIS, THEN GO TO 'RunTests.py' AND REMOVE THIS WARNING AFTER YOU'VE LOOKED THE FILE OVER TO MAKE SURE IT WON'T START CREATING FILES IN STRANGE PLACES, ETC."))
    input()
    sys.exit(1)

# Prompt the user before running tests
# (in the future, we'll ask which tests to run)
do_we_run = testmiscstuff.run_prompt()
if do_we_run is False:
    sys.exit()
# TODO: Add ability to pick and choose which tests to run
t0 = time.perf_counter()

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
# Running sanity test, performance test, and saving output to file
os.chdir (TESTLOG_DIR)
print ("Running sanity tests... ", end="")
with open(DATESTRING_SHORT + ".sanity.txt", "w+") as f:
    # Save original stdout and stderr settings
    _old_stdout = sys.stdout
    _old_stderr = sys.stderr
    # Switch stdout and stderr to file output
    sys.stdout = f
    sys.stderr = f

    print (PROJECT_NAME, "test suite results")
    print (DATESTRING)
    testmiscstuff.logformat_line ()
    testmiscstuff.logformat_header ("GENERATOR SANITY TEST")
    print ()
    testsuite = unittest.TestLoader().loadTestsFromModule(testfunctions)
    unittest.TextTestRunner().run(testsuite)

    # Restore stdout and stderr to original settings
    sys.stderr = _old_stderr
    sys.stdout = _old_stdout
print ("done.")

# Running performance tests...
os.chdir (TESTLOG_DIR)
print ("Running performance tests... ", end="")
with open(DATESTRING_SHORT + ".perf.txt", "w+") as f:
    # Save original stdout and stderr settings
    _old_stdout = sys.stdout
    _old_stderr = sys.stderr
    # Switch stdout and stderr to file output
    sys.stdout = f
    sys.stderr = f

    print (PROJECT_NAME, "test suite results")
    print (DATESTRING)
    testmiscstuff.logformat_line ()
    testmiscstuff.logformat_header ("PERFORMANCE TEST FULL RESULTS")
    print ()
    print ("Rosevomit's performance when generating 10 names (measured in seconds)")
    with testmiscstuff.Suppressor():
        perftest10_results = timetest_name_generation (ARG_number_of_names=10)
    for key, value in perftest10_results.items():
        print (f"   {key}: {value}")
    print ()
    print ("Rosevomit's performance when generating 100 names (measured in seconds)")
    with testmiscstuff.Suppressor():
        perftest100_results = timetest_name_generation (ARG_number_of_names=100)
    for key, value in perftest100_results.items():
        print (f"   {key}: {value}")
    print ()
    print ("Rosevomit's performance when generating 1,000 names (measured in seconds)")
    with testmiscstuff.Suppressor():
        perftest1000_results = timetest_name_generation (ARG_number_of_names=1000)
    for key, value in perftest1000_results.items():
        print (f"   {key}: {value}")

    # Restore stdout and stderr to original settings
    sys.stderr = _old_stderr
    sys.stdout = _old_stdout
print ("done.")

"""
# TODO: The imports module thing doesn't seem to be working. Need to fix this.
# Generating "imports" results file
if FINDIMPORTS_MODULE_EXISTS is True:
    print ("Generating import list... ", end="")
    os.chdir (TESTLOG_DIR)
    with open(DATESTRING_SHORT + ".imports.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        testmiscstuff.logformat_line ()
        testmiscstuff.logformat_header ("full imports list")
        os.chdir (ROSEVOMIT_DIR)
        mock_cli_args = ["rosevomit.py", "-i"]
        findimports.main(argv=mock_cli_args)

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    print ("done.")
else:
    print ("The 'findimports' module is not present.")
    print ("An import list will not be generated for this test.")

# Generating "unused imports" results file
if FINDIMPORTS_MODULE_EXISTS is True:
    print ("Generating unused import list... ", end="")
    os.chdir (TESTLOG_DIR)
    with open(DATESTRING_SHORT + ".imports-unused.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        testmiscstuff.logformat_line ()
        testmiscstuff.logformat_header ("UNUSED IMPORTS LIST")
        os.chdir (ROSEVOMIT_DIR)
        mock_cli_args = ["rosevomit.py", "-i", "-u"]
        findimports.main(argv=mock_cli_args)

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    print ("done")
else:
    print ("The 'findimports' module is not present.")
    print ("An unused imports list will not be generated for this test.")
"""

# Generating summary file
t1 = time.perf_counter()
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
    if FINDIMPORTS_MODULE_EXISTS is False:
        print (textwrap.fill ("The third-party module 'findimports' was not present, therefore the following tests were not run: import list, unused imports list"))
    testtime = t1 - t0
    display_testtime = round (testtime, ndigits=1)
    # For explanations of the '//' and '%' operators, see here: https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
    display_minutes = int (testtime // 60)
    display_seconds = round ((testtime % 60), ndigits=1)
    print (f"Time to run tests: {display_testtime} seconds, or")
    print (f"                   {display_minutes} minutes, {display_seconds} seconds")

    testmiscstuff.logformat_line ()
    testmiscstuff.logformat_header ("GENERATOR SANITY TEST")
    print ("Blah blah blah.")

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


if PYLINT_MODULE_EXISTS:
    print ("Running pylint... ", end="")
    os.chdir (TESTLOG_DIR)
    with open(DATESTRING_SHORT + ".pylint.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        testmiscstuff.logformat_line ()
        testmiscstuff.logformat_header ("pylint")
        os.chdir (REPO_DIR)
        # pylint error messages
        #   C0301 line-too-long
        #   C0326 spaces
        #   E0401 import-error (because they don't seem to work properly when running statically)
        pylint_opts = ["rosevomit", "--disable=C0301,C0326,E0401", "--reports=yes"]
        linter.Run (pylint_opts)  # BUG: The script seems to end here, after this linter report successfully runs. Need to find out why.

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    print ("done.")
else:
    print ("The 'pylint' module is not present.")
    print ("A pylint report will not be generated for this test.")

print ()
print ("Testing complete. One or more text files with the test results have")
print ("been placed in:")
print ("  ", TESTLOG_DIR)
print ()
