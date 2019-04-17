# ****THIS IS A PUBLIC SERVICE ANNOUCEMENT****
# STANDARD PSEUDO-RANDOM GENERATORS (LIKE THE ONE USED IN THIS SCRIPT) ARE NOT SUITABLE FOR SECURITY/CRYPTOGRAPHIC PURPOSES.

# Imports the "lib/random.py" module. This is an external Python library that we will use to pick
# one or more elements randomly from a list. By default, it seeds itself from the current system time.
# We need this to use the "random.choice()" and "random.choices()" functions later in this file.
import random

# We define a list (an "array") of items.
exampleArray = ['a', 'b', 'c', 'd', 'e',]

# We pick an item of the list at random, and display it on the screen.
print ( random.choice(exampleArray) )
