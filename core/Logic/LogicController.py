# --------------------
# LogicController.py
# --------------------
# This is the main "logic" file for Alex's "Project Rosevomit", a random name generator written in Python. Its job is to keep track of the program's custom logic modules and to serve as an intermediary in between them and the main file (rosevomit.py). This isn't actually necessary, but it serves as good coding practice for me. Hopefully.

import textwrap

# This section determines if this module is running on its own, if it is being invoked from another module. If it is running on its own, it can import 'RandomName' without any additional specific instructions. If it is being run from another module, however, it needs to specify that it is trying to import the 'RandomName' from the 'Logic' package. Note that for the \Logic directory to be considered a package, it needs to contain an __init__.py file.
if __name__ == "__main__":
    import RandomEvent
    import RandomName
    import RepeatFunction
else:
    from logic import RandomEvent, RandomName, RepeatFunction


def printLC(x, end="\n"):
    """Applies a consistant format to LogicController's text output."""
    print ("   LOGIC CONTROLLER:", x, end=end)


def setup():
    print ()
    printLC ("Present and accounted for.")
    print ()


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

    elif x == "globalevents":
        def get_events(_timelineYear):
            events = []
            print (f"{_timelineYear} years ago, scholars tell us...")
            events.extend (RandomEvent.check_volcano ())
            for item in range (len (events)):
                print (textwrap.fill (f"    {events[item]}", width=70)),
        RepeatFunction.repeat_decrement (get_events, y)
    else:
        printLC ("I'm sorry, I can't do that.")
