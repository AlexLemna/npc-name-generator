# LIBRARIES AND MODULES
#
# for access to the filesystem and for some useful functions on pathnames
from pathlib import Path
# and for an additional useful function for changing directories
from os import chdir


## Print the current working directory and home directory on screen so I can confirm them visually.
print(f"Current directory: {Path.cwd()}")
print(f"Home directory: {Path.home()}")
chdir('..')
print(f"New current directory: {Path.cwd()}")

# make a shortcut variable for the current working directory path
path = Path.cwd()

# declare some more variables and set them to the expected paths of the UI, Logic, and Data folders. 
# We'll use these variables as quick ways to interact with files and folders outside our current working directory.
uiDirectory = path / 'UI'
logicDirectory = path / 'Logic'
dataDirectory = path / 'Data'

# Print the directory paths on screen so I can confirm them visually.
print(uiDirectory)
print(logicDirectory)
print(dataDirectory)

#################
# x = 1
# y = 2

# if x == y:
#    print("Got it.") 
# elif x != y:
#    print("Error. I can't find the Data folder.")
# else:
#    print("An impossible error occured.")

# TUTORIALS
# I got this from here: https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
# also: http://zetcode.com/python/pathlib/
 