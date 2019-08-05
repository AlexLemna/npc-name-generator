# rosevomit/core/Utilities.py
# For those little code snippets that don't make sense going anywhere else.


def CWD_home():
    """Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory"""
    os.chdir (os.path.dirname (sys.argv[0]))
