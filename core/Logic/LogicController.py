# --------------------
# LogicController.py
# --------------------
# This is the main "logic" file for Alex's "Project Rosevomit", a random name generator written in Python. Its job is to keep track of the program's custom logic modules and to serve as an intermediary in between them and the main file (rosevomit.py). This isn't actually necessary, but it serves as good coding practice for me. Hopefully.

import textwrap

# This section determines if this module is running on its own, if it is being invoked from another module. If it is running on its own, it can import 'rlRandomName' without any additional specific instructions. If it is being run from another module, however, it needs to specify that it is trying to import the 'rlRandomName' from the 'Logic' package. Note that for the \Logic directory to be considered a package, it needs to contain an __init__.py file.
if __name__ == "__main__":
    import rlRandomName
    import rlRepeatFunction
else:
    from Logic import rlRandomName, rlRepeatFunction


def printLC(x, end = "\n"): # Applies a consistant format to LogicController's text output.
    print ("   LOGIC CONTROLLER:", x, end = end)

def setup():
    print ()
    printLC ("Present and accounted for.")
    print()

def gen(x):
    if x == "first":
        output = rlRandomName.twofiles("NamesFirstFemale.txt", "NamesFirstMale.txt")
        print ( output )
    elif x == "firstfemale":
        output = rlRandomName.onefile("NamesFirstFemale.txt")
        print ( output )
    elif x == "firstmale":
        output = rlRandomName.onefile("NamesFirstMale.txt")
        print ( output )
    elif x == "last":
        output = rlRandomName.onefile("NamesLast.txt")
        print ( output )
    elif x == "full":
        output = rlRandomName.twofiles("NamesFirstFemale.txt", "NamesFirstMale.txt")
        output1 = rlRandomName.onefile("NamesLast.txt")
        print ( output, output1 )
    elif x == "fullfemale":
        output = rlRandomName.onefile("NamesFirstFemale.txt")
        output1 = rlRandomName.onefile("NamesLast.txt")
        print ( output, output1 )
    elif x == "fullmale":
        output = rlRandomName.onefile("NamesFirstMale.txt")
        output1 = rlRandomName.onefile("NamesLast.txt")
        print ( output, output1 )
    elif x == "Sample" or x == "sample":
        output = rlRandomName.SampleData()
        print ( output )
    else:
        printLC ("I'm sorry, I can't do that.")

# Sdef repeatFunction (x, y)