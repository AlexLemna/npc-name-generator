import os
import platform
import statistics
import sys
import textwrap
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

# --------------------- SANITY TEST ---------------------
def sanity(ARG_test_directory, ARG_datestring: str, ARG_short_datestring: str, ARG_project: str):
    os.chdir (ARG_test_directory)
    print ("Running sanity tests... ", end="")
    with open(ARG_short_datestring + ".sanity.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (ARG_project, "test suite results")
        print (ARG_datestring)
        testmiscstuff.logformat_line ()
        testmiscstuff.logformat_header ("GENERATOR SANITY TEST")
        print ()
        testsuite = unittest.TestLoader().loadTestsFromModule(testfunctions)
        unittest.TextTestRunner().run(testsuite)

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    print ("done.")


# --------------------- PERFORMANCE TEST ---------------------
def performance(ARG_test_directory, ARG_datestring: str, ARG_short_datestring: str, ARG_project: str):
    os.chdir (ARG_test_directory)
    print ("Running performance tests... ", end="")
    with open(ARG_short_datestring + ".perf.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (ARG_project, "test suite results")
        print (ARG_datestring)
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
    return perftest10_results, perftest100_results, perftest1000_results


# --------------------- IMPORTS TEST ---------------------
# TODO: The imports module thing doesn't seem to be working. Need to fix this.
def imports(ARG_test_directory, ARG_rosevomit_directory, ARG_datestring: str, ARG_short_datestring: str, ARG_project: str):
    if FINDIMPORTS_MODULE_EXISTS is True:
        print ("Generating import list... ", end="")
        os.chdir (ARG_test_directory)
        with open(ARG_short_datestring + ".imports.txt", "w+") as f:
            # Save original stdout and stderr settings
            _old_stdout = sys.stdout
            _old_stderr = sys.stderr
            # Switch stdout and stderr to file output
            sys.stdout = f
            sys.stderr = f

            print (ARG_project, "test suite results")
            print (ARG_datestring)
            testmiscstuff.logformat_line ()
            testmiscstuff.logformat_header ("full imports list")
            os.chdir (ARG_rosevomit_directory)
            mock_cli_args = ["rosevomit.py", "-i"]
            findimports.main(argv=mock_cli_args)

            # Restore stdout and stderr to original settings
            sys.stderr = _old_stderr
            sys.stdout = _old_stdout
        print ("done.")
    else:
        print ("The 'findimports' module is not present.")
        print ("An import list will not be generated for this test.")


# --------------------- UNUSED IMPORTS TEST ---------------------
# TODO: The imports module thing doesn't seem to be working. Need to fix this.
def unused_imports(ARG_test_directory, ARG_rosevomit_directory, ARG_datestring: str, ARG_short_datestring: str, ARG_project: str):
    if FINDIMPORTS_MODULE_EXISTS is True:
        print ("Generating unused import list... ", end="")
        os.chdir (ARG_test_directory)
        with open(ARG_short_datestring + ".imports-unused.txt", "w+") as f:
            # Save original stdout and stderr settings
            _old_stdout = sys.stdout
            _old_stderr = sys.stderr
            # Switch stdout and stderr to file output
            sys.stdout = f
            sys.stderr = f

            print (ARG_project, "test suite results")
            print (ARG_datestring)
            testmiscstuff.logformat_line ()
            testmiscstuff.logformat_header ("UNUSED IMPORTS LIST")
            os.chdir (ARG_rosevomit_directory)
            mock_cli_args = ["rosevomit.py", "-i", "-u"]
            findimports.main(argv=mock_cli_args)

            # Restore stdout and stderr to original settings
            sys.stderr = _old_stderr
            sys.stdout = _old_stdout
        print ("done")
    else:
        print ("The 'findimports' module is not present.")
        print ("An unused imports list will not be generated for this test.")


# --------------------- PYTLINT TEST ---------------------
def pylint(ARG_test_directory, ARG_repository_directory, ARG_datestring: str, ARG_short_datestring: str, ARG_project: str):
    if PYLINT_MODULE_EXISTS:
        print ("Running pylint... ", end="")
        os.chdir (ARG_test_directory)
        with open(ARG_short_datestring + ".pylint.txt", "w+") as f:
            # Save original stdout and stderr settings
            _old_stdout = sys.stdout
            _old_stderr = sys.stderr
            # Switch stdout and stderr to file output
            sys.stdout = f
            sys.stderr = f

            print (ARG_project, "test suite results")
            print (ARG_datestring)
            testmiscstuff.logformat_line ()
            testmiscstuff.logformat_header ("pylint")
            os.chdir (ARG_repository_directory)
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


# --------------------- SUMMARY REPORT ---------------------
def summary(ARG_test_directory, ARG_datestring: str, ARG_short_datestring: str, ARG_project: str, ARG_directories_present, ARG_directories_missing, ARG_time, ARG_perfresults_10, ARG_perfresults_100, ARG_perfresults_1000):
    os.chdir (ARG_test_directory)
    print ("Writing summary file... ", end="")
    with open(ARG_short_datestring + ".summary.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (ARG_project, "test suite results")
        print (ARG_datestring)
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
        print ("Directories found:", len (ARG_directories_present))
        for item in ARG_directories_present:
            print ("  ", item)
        print ()
        print ("Directories not found:", len (ARG_directories_missing))
        for item in ARG_directories_missing:
            print ("  ", item)
        print ()
        if FINDIMPORTS_MODULE_EXISTS is False:
            print (textwrap.fill ("The third-party module 'findimports' was not present, therefore the following tests were not run: import list, unused imports list"))
        testtime = ARG_time
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
        for key, value in ARG_perfresults_10.items():
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
        for key, value in ARG_perfresults_100.items():
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
        for key, value in ARG_perfresults_1000.items():
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
