import os
import sys
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
from constants import DATESTRING, DATESTRING_SHORT, PROJECT_NAME
from performancetests import timetest_name_generation
import testfunctions
import testmiscstuff
# Rosevomit itself
from context import rosevomit

# --------------------- SANITY TEST ---------------------
def sanity(ARG_test_directory):
    os.chdir (ARG_test_directory)
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


# --------------------- PERFORMANCE TEST ---------------------
def performance(ARG_test_directory):
    os.chdir (ARG_test_directory)
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
    return perftest10_results, perftest100_results, perftest1000_results


# --------------------- IMPORTS TEST ---------------------
def imports(ARG_test_directory, ARG_rosevomit_directory):
    if FINDIMPORTS_MODULE_EXISTS is True:
        os.chdir (ARG_test_directory)
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
            os.chdir (ARG_rosevomit_directory)
            mock_cli_args = ["rosevomit.py", "-i"]
            findimports.main(argv=mock_cli_args)

            # Restore stdout and stderr to original settings
            sys.stderr = _old_stderr
            sys.stdout = _old_stdout
    else:
        raise ImportError



# --------------------- UNUSED IMPORTS TEST ---------------------
def unused_imports(ARG_test_directory, ARG_rosevomit_directory):
    if FINDIMPORTS_MODULE_EXISTS is True:
        os.chdir (ARG_test_directory)
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
            os.chdir (ARG_rosevomit_directory)
            mock_cli_args = ["rosevomit.py", "-i", "-u"]
            findimports.main(argv=mock_cli_args)

            # Restore stdout and stderr to original settings
            sys.stderr = _old_stderr
            sys.stdout = _old_stdout
    else:
        raise ImportError


# --------------------- PYTLINT TEST ---------------------
def pylint(ARG_test_directory, ARG_repository_directory):
    if PYLINT_MODULE_EXISTS is True:
        os.chdir (ARG_test_directory)
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
            os.chdir (ARG_repository_directory)
            # pylint error messages
            #   C0301 line-too-long
            #   C0326 spaces
            #   E0401 import-error (because they don't seem to work properly when running statically)
            pylint_opts = ["rosevomit", "--disable=C0301,C0326,E0401", "--reports=yes"]
            linter.Run (pylint_opts, do_exit=False)

            # Restore stdout and stderr to original settings
            sys.stderr = _old_stderr
            sys.stdout = _old_stdout
    else:
        raise ImportError
