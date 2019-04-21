import pathlib
import random

# Defining empty list. Explicit variable declaration isn't necessary in Python, but I like it.
contents = []

# target files is at "F:\OneDrive\CODE\Projects\npc-name-generator\Data\simple data\sample.txt"
with open('local-test-data.txt', 'r') as fileData:
    contents = fileData.readlines()

random.choice(contents)