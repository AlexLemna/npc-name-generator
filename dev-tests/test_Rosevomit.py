from io import StringIO
import random
import sys
import unittest

from logic import LogicController


class RosevomitTestCase(unittest.TestCase):
    """Tests for 'Rosevomit.py'."""

    def test_name_generation(self):
        """Do we get the number of names we expect?"""
        number_names_to_generate = random.randint (2, 200)
        old_stdout = sys.stdout

        test_stdout = StringIO()  # io.StringIO is in-memory stream for text I/O.
        sys.stdout = test_stdout  # Redirecting stdout to stream.
        LogicController.gen ("first", number_names_to_generate)  # Actually running test

        sys.stdout = old_stdout  # Resetting stdout to print to terminal again
        result = test_stdout.getvalue()  # Reading the test results from memory
        names_generated = result.split('\n')
        if names_generated[-1] == "":   # Sometimes the results end with a blank line.
            del names_generated[-1]     # We get rid of that.
        else:
            pass
        self.assertEqual (number_names_to_generate, len (names_generated))
        # Now, need to add similar tests for the rest of 'LogicController.gen'

unittest.main()
