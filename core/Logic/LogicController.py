# --------------------
# LogicController.py
# --------------------
# This is the main "logic" file for Alex's "Project Rosevomit", a random name generator written in Python. Its job is to keep track of the program's custom logic modules and to serve as an intermediary in between them and the main file (rosevomit.py). This isn't actually necessary, but it serves as good coding practice for me. Hopefully.

from inspect import currentframe, getframeinfo
import os
import sys
import textwrap

# This section determines if this module is running on its own, if it is being invoked from another module. If it is running on its own, it can import 'RandomName' without any additional specific instructions. If it is being run from another module, however, it needs to specify that it is trying to import the 'RandomName' from the 'Logic' package. Note that for the \Logic directory to be considered a package, it needs to contain an __init__.py file.
if __name__ == "__main__":
    import RandomEvent
    import RandomName
    import RepeatFunction
    import WorkWithProgramFiles
    from errors import CustomErrors
else:
    from errors import CustomErrors
    from logic import RandomEvent, RandomName, RepeatFunction, WorkWithProgramFiles


def gen(x, y):
    """This function receives the user input and calls functions accordingly."""
    if x == "first":
        def get_names():
            output = RandomName.two_files ("USCensusNamesFirstFemale.txt", "USCensusNamesFirstMale.txt")
            print (output)
        RepeatFunction.repeat (get_names, y)

    elif x == "firstfemale":
        def get_names():
            output = RandomName.one_file ("USCensusNamesFirstFemale.txt")
            print (output)
        RepeatFunction.repeat (get_names, y)

    elif x == "firstmale":
        def get_names():
            output = RandomName.one_file ("USCensusNamesFirstMale.txt")
            print (output)
        RepeatFunction.repeat (get_names, y)

    elif x == "last":
        def get_names():
            output = RandomName.one_file ("USCensusNamesLast.txt")
            print (output)
        RepeatFunction.repeat (get_names, y)

    elif x == "full":
        def get_names():
            output = RandomName.two_files ("USCensusNamesFirstFemale.txt", "USCensusNamesFirstMale.txt")
            output1 = RandomName.one_file ("USCensusNamesLast.txt")
            print (output, output1)
        RepeatFunction.repeat (get_names, y)

    elif x == "fullfemale":
        def get_names():
            output = RandomName.one_file ("USCensusNamesFirstFemale.txt")
            output1 = RandomName.one_file ("USCensusNamesLast.txt")
            print (output, output1)
        RepeatFunction.repeat (get_names, y)

    elif x == "fullmale":
        def get_names():
            output = RandomName.one_file ("USCensusNamesFirstMale.txt")
            output1 = RandomName.one_file ("USCensusNamesLast.txt")
            print (output, output1)
        RepeatFunction.repeat (get_names, y)

    else:
        print ("I'm sorry, I can't do that.")
        # TODO: define a custom error message, and raise it here.


def gen_timeline(eventtypes, yearrange):
    """This function receives the user input and calls functions accordingly."""
    if eventtypes == "globalevents":
        def get_events(timelineYear, output_file):
            """This function checks to see what events have happened in a given year. It assumes that the probability of events does not change from year to year."""
            events = []
            print (f"{timelineYear} years ago, scholars tell us...")
            # Run checks to generate events. The RandomEvent checks return a list whose
            # elements are the event text of events that occured. We add these elements
            # to the "events" list.
            events.extend (RandomEvent.check_volcano (timelineYear, csv_destination=output_file))
            events.extend (RandomEvent.check_earthquake (timelineYear, csv_destination=output_file))
            events.extend (RandomEvent.check_impact (timelineYear, csv_destination=output_file))
            events.extend (RandomEvent.check_astronomy (timelineYear, csv_destination=output_file))
            for item in range (len (events)):
                print (textwrap.fill (f"    {events[item]}", width=70))
                print ()

        try:
            try:
                os.chdir ("./temp/")
            except FileNotFoundError:
                os.chdir ("..")
                os.chdir ("./temp")
        except FileNotFoundError:  # Maybe it's being run by a testing script?
            os.chdir ("..")
            os.chdir ("./core/temp/")
        _tempfile_name = WorkWithProgramFiles.setname()
        _tempfile = open(_tempfile_name, "a+")

        for item in range (0, yearrange):
            get_events (timelineYear=yearrange, output_file=_tempfile_name)
            yearrange = (yearrange - 1)

        _tempfile.write ("Testing.")
        _tempfile.close()
    else:
        print ("I'm sorry, I can't do that.")
        # TODO: define a custom error message, and raise it here.
