# We have a file named ExampleList.txt in the same directory as this file. This script loads that file, reads it, and loads it into a list named exampleArray.
# We use the readlines() function - it's a function that doesn't take any arguments, it just reads the specified file line by line into a list of strings.

# Import the "lib/random.py" module. We will use the "random.choice()" and "random.choices()" functions in this file.
import random
    # By default, it seeds itself from the current system time.


# define empty list (explicit variable declaration isn't necessary in Python, but I like it)
exampleArray = []

# open file and read the content into a list 'exampleArray'
with open('ExampleList.txt', 'r') as fileData: 
    exampleArray = fileData.readlines()

# We pick an item of the list at random, and display it on the screen.
print ( random.choice(exampleArray) )





# END OF SCRIPT

# PYTHON TUTORIALS USED
    # Loading a file into a list: http://openbookproject.net/pybiblio/tips/wilson/loadingfile.php
    # Interacting with files with more human-readable code: https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/

# ****THIS IS A PUBLIC SERVICE ANNOUCEMENT****
# STANDARD PSEUDO-RANDOM GENERATORS (LIKE THE ONE USED IN THIS SCRIPT) ARE NOT SUITABLE FOR SECURITY/CRYPTOGRAPHIC PURPOSES.