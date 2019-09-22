from io import StringIO
import random
import sys
import unittest

# Import Rosevomit for testing
from context import rosevomit
from rosevomit import programlogic

# ---------- Helper functions ----------
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


def validate_string_cleaning (testcaseself, target_string: str):
    """Do we find forbidden characters?"""
    bad_characters = ("\n", "\r")
    for item in bad_characters:
        testcaseself.assertNotIn (item, target_string)
    # Checking for beginning or ending spaces
    firstcharacter = target_string[0]
    lastcharacter = target_string[-1]
    testcaseself.assertNotEqual (firstcharacter, " ")
    testcaseself.assertNotEqual (lastcharacter, " ")


# ---------- Unit tests ----------
class LowLevelTests (unittest.TestCase):
    """Testing various low level functions in Rosevomit."""
    def test_func_one_file (self):
        """Does one_file() return a string without newlines and spaces?"""
        result = rosevomit.programlogic.randomname.one_file ("SampleData.txt")
        # Checking that it returns a string
        self.assertIsInstance (result, str)
        validate_string_cleaning (self, result)


    def test_func_two_files (self):
        """Does two_files() return a string without newlines and spaces?"""
        result = rosevomit.programlogic.randomname.two_files ("SampleData.txt", "SampleData2.txt")
        # Checking that it returns a string
        self.assertIsInstance (result, str)
        validate_string_cleaning (self, result)


class NameGenerationTests (unittest.TestCase):
    """Testing Rosevomit's name generation feature."""
    def test_name_generation (self):
        """Do we get the number of names we expect?"""
        keyword_list = ["first", "firstfemale", "firstmale", "last", "full", "fullfemale", "fullmale"]
        for keyword in keyword_list:
            test_string_generation (self, keyword)


if __name__ == "__main__":
    unittest.main()
