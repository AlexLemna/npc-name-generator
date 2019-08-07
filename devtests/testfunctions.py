from io import StringIO
import random
import sys
import unittest

# Import Rosevomit for testing
from context import rosevomit
from rosevomit import programlogic


def test_string_generation (testcaseself, keyword: str):
    """Do we get the number of items we expect?"""
    number_names_to_generate = random.randint (2, 200)
    old_stdout = sys.stdout

    test_stdout = StringIO()  # io.StringIO is in-memory stream for text I/O.
    sys.stdout = test_stdout  # Redirecting stdout to stream.
    rosevomit.programlogic.logiccontroller.gen (keyword, number_names_to_generate)  # Actually running test

    sys.stdout = old_stdout  # Resetting stdout to print to terminal again
    result = test_stdout.getvalue()  # Reading the test results from memory
    names_generated = result.split('\n')
    if names_generated[-1] == "":   # Sometimes the results end with a blank line.
        del names_generated[-1]     # We get rid of that.
    else:
        pass
    testcaseself.assertEqual (number_names_to_generate, len (names_generated))


class NameGenerationTests(unittest.TestCase):
    """Tests for 'Rosevomit.py'."""
    def test_name_generation(self):
        """Do we get the number of names we expect?"""
        keyword_list = ["first", "firstfemale", "firstmale", "last", "full", "fullfemale", "fullmale"]
        for keyword in keyword_list:
            test_string_generation (self, keyword)


if __name__ == "__main__":
    unittest.main()
