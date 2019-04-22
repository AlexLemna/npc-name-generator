# --------------------
# LogicController.py
# --------------------
# This is the main "logic" file for Alex's "Project Rosa", a random name generator written in Python. Its job is to keep track of the program's custom logic modules and to serve as an intermediary in between them and the main file (rosa.py). This isn't actually necessary, but it serves as good coding practice for me. Hopefully.

# import pathlib
# import os
# import sys
import textwrap

def printLC(x, end = "\n"): # Applies a consistant format to LogicController's text output.
    print ("   LOGIC CONTROLLER:", x, end = end)

print ()
printLC ("Present and accounted for.")
printLC ( "Importing my modules...", "")

# This section determines if this module is running on its own, if it is being invoked from another module. If it is running on its own, it can import 'rlRandomName' without any additional specific instructions. If it is being run from another module, however, it needs to specify that it is trying to import the 'rlRandomName' from the 'Logic' package. Note that for the \Logic directory to be considered a package, it needs to contain an __init__.py file.
if __name__ == "__main__":
    import rlRandomName
else:
    from Logic import rlRandomName

print ("done. ")
printLC ("LogicController setup complete.")
print()

print ("Let's run rlRandomName.py.")
output = rlRandomName.SampleData()
print ( output )
