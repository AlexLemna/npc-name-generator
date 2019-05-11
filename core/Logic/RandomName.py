# ----------------------------------------
# RandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for randomly generating names.

import os
import random
import sys
from inspect import currentframe, getframeinfo

contents = []


def CWD_home():
    """Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory"""
    os.chdir (os.path.dirname (sys.argv[0]))


def one_file (x):
    """A function that returns one random line from a text file 'x'"""
    CWD_home ()
    if __name__ == "logic.RandomName":  # This is the normal module behavior - it's being run from somewhere else.
        os.chdir ("./Data")
        with open (x, 'r') as fileData:
            contents = fileData.readlines()
            contents = [item.rstrip() for item in contents]  # strips newline characters ('\n') and spaces
            return (random.choice (contents))

    elif __name__ == "__main__":  # Checks if this program is running as the main script (only happens for debugging purposes)
        os.chdir ("..")
        os.chdir ("./Data")
        with open (x, 'r') as fileData:
            contents = fileData.readlines()
            contents = [item.rstrip() for item in contents]  # strips newline characters ('\n') and spaces
            print (random.choice (contents))

    elif __name__ == "RandomName":  # Checks if this program is running as a module from another script inside its home directory (only happens for debugging purposes)
        os.chdir ("..")
        os.chdir ("./Data")
        with open (x, 'r') as fileData:
            contents = fileData.readlines()
            contents = [item.rstrip() for item in contents]  # strips newline characters ('\n') and spaces
            return (random.choice (contents))

    else:  # I'm honestly not sure what situation wouldn't fit into the statements above.
        frameinfo = getframeinfo (currentframe())

        print ("")
        print ("A wild UNEXPECTED ERROR appeared!")
        print (f"REF: The file location is {frameinfo.filename}.")
        print (f"REF: This error message is around line {frameinfo.lineno} of that file.")
        print ("   SUMMARY:")
        print ("   This section of code has some 'if' and 'else if' statements that should")
        print ("   cover every situation. This error is the 'else' statement, and it means")
        print ("   a situation occured that I didn't forsee.")
        print ("   SPECIFICS:")
        print ("   The error occured in a file called 'RandomName.py'. The file behaves")
        print ("   differently depending on if it is running by itself or as a 'module' being")
        print ("   called by a different file. It can tell how it is being run by checking")
        print ("   a variable called __name__ against some predetermined values. It expects")
        print ("   __name__'s value to be 'RandomName', 'logic.RandomName', or '__main__'.")
        print (f"   Instead, the value is '{__name__}'.")
        print ("   WHAT YOU SHOULD DO:")
        print ("   Take a screenshot and contact Alex. Also, tell him to create some kind of")
        print ("   error logging system so you don't have to manually ask him for help every")
        print ("   time he messes up.")


def two_files (file1, file2):
    """A function that returns one random line from a list generated from multiple text files 'x', 'y', and so on."""
    CWD_home ()
    if __name__ == "logic.RandomName":  # This is the normal module behavior - it's being run from somewhere else.
        os.chdir ("./Data")
        fileData1 = open (file1, 'r')
        contents1 = fileData1.readlines()
        contents1 = [item.rstrip() for item in contents1]  # strips newline characters ('\n') and spaces
        fileData1.close()
        fileData2 = open (file2, 'r')
        contents2 = fileData2.readlines()
        contents2 = [item.rstrip() for item in contents2]
        fileData2.close()
        contents = contents1 + contents2
        return (random.choice (contents))

    elif __name__ == "__main__":  # Checks if this program is running as the main script (only happens for debugging purposes)
        os.chdir ("..")
        os.chdir ("./Data")
        fileData1 = open (file1, 'r')
        contents1 = fileData1.readlines()
        contents1 = [item.rstrip() for item in contents1]  # strips newline characters ('\n') and spaces
        fileData1.close()
        fileData2 = open (file2, 'r')
        contents2 = fileData2.readlines()
        contents2 = [item.rstrip() for item in contents2]
        fileData2.close()
        contents = contents1 + contents2
        return (random.choice (contents))

    elif __name__ == "RandomName":  # Checks if this program is running as a module from another script inside its home directory (only happens for debugging purposes)
        os.chdir ("..")
        os.chdir ("./Data")
        fileData1 = open (file1, 'r')
        contents1 = fileData1.readlines()
        contents1 = [item.rstrip() for item in contents1]  # strips newline characters ('\n') and spaces
        fileData1.close()
        fileData2 = open (file2, 'r')
        contents2 = fileData2.readlines()
        contents2 = [item.rstrip() for item in contents2]
        fileData2.close()
        contents = contents1 + contents2
        return (random.choice (contents))

    else:  # I'm honestly not sure what situation wouldn't fit into the statements above.
        frameinfo = getframeinfo (currentframe())

        print ("")
        print ("A wild UNEXPECTED ERROR appeared!")
        print (f"REF: The file location is {frameinfo.filename}.")
        print (f"REF: This error message is around line {frameinfo.lineno} of that file.")
        print ("   SUMMARY:")
        print ("   This section of code has some 'if' and 'else if' statements that should")
        print ("   cover every situation. This error is the 'else' statement, and it means")
        print ("   a situation occured that I didn't forsee.")
        print ("   SPECIFICS:")
        print ("   The error occured in a file called 'RandomName.py'. The file behaves")
        print ("   differently depending on if it is running by itself or as a 'module' being")
        print ("   called by a different file. It can tell how it is being run by checking")
        print ("   a variable called __name__ against some predetermined values. It expects")
        print ("   __name__'s value to be 'RandomName', 'logic.RandomName', or '__main__'.")
        print (f"   Instead, the value is '{__name__}'.")
        print ("   WHAT YOU SHOULD DO:")
        print ("   Take a screenshot and contact Alex. Also, tell him to create some kind of")
        print ("   error logging system so you don't have to manually ask him for help every")
        print ("   time he messes up.")


def sample_file ():
    """A function that returns one random line from a text file at /Data/SampleData.txt"""
    CWD_home()
    if __name__ == "logic.RandomName":  # This is the normal module behavior - it's being run from somewhere else.
        os.chdir ("./Data")
        with open('SampleData.txt', 'r') as fileData:
            contents = fileData.readlines()
            return (random.choice (contents))

    elif __name__ == "__main__":  # Checks if this program is running as the main script (only happens for debugging purposes)
        os.chdir ("..")
        os.chdir ("./Data")
        with open('SampleData.txt', 'r') as fileData:
            contents = fileData.readlines()
            print (random.choice (contents))

    elif __name__ == "RandomName":  # Checks if this program is running as a module from another script inside its home directory (only happens for debugging purposes)
        os.chdir ("..")
        os.chdir ("./Data")
        with open('SampleData.txt', 'r') as fileData:
            contents = fileData.readlines()
            return (random.choice (contents))

    else:  # I'm honestly not sure what situation wouldn't fit into the statements above.
        frameinfo = getframeinfo (currentframe())

        print ("")
        print ("A wild UNEXPECTED ERROR appeared!")
        print (f"REF: The file location is {frameinfo.filename}.")
        print (f"REF: This error message is around line {frameinfo.lineno} of that file.")
        print ("   SUMMARY:")
        print ("   This section of code has some 'if' and 'else if' statements that should")
        print ("   cover every situation. This error is the 'else' statement, and it means")
        print ("   a situation occured that I didn't forsee.")
        print ("   SPECIFICS:")
        print ("   The error occured in a file called 'RandomName.py'. The file behaves")
        print ("   differently depending on if it is running by itself or as a 'module' being")
        print ("   called by a different file. It can tell how it is being run by checking")
        print ("   a variable called __name__ against some predetermined values. It expects")
        print ("   __name__'s value to be 'RandomName', 'logic.RandomName', or '__main__'.")
        print (f"   Instead, the value is '{__name__}'.")
        print ("   WHAT YOU SHOULD DO:")
        print ("   Take a screenshot and contact Alex. Also, tell him to create some kind of")
        print ("   error logging system so you don't have to manually ask him for help every")
        print ("   time he messes up.")
