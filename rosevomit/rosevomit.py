# --------------------
# ROSEVOMIT.PY
# --------------------
# The main file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python.

print ()
print ("Starting ROSEVOMIT.")
# MODULES FROM PYTHON'S STANDARD LIBRARY
import os
import sys

# INTERNAL MODULES
from core import settings, startup
from programcli import dialogexit, worsecli


HOME_DIRECTORY = os.path.dirname (sys.argv[0])

if settings.existence() is False:
    print ("The settings don't exist. Recreating settings file at:")
    print (f"  {settings.SETTINGS_FILE}")
    settings.restore_file()
    print ()
else:
    pass
startup.main_setup(HOME_DIRECTORY)

print ()
print (69 * "-")
print (27 * "-", "ROSEVOMIT.PY", 28 * "-")
print (69 * "-")
print ()

# After setup, rosevomit.py will display the main menu and will carry out instructions based on user input. This is an infinite loop - if rosevomit.py ever has no more instructions to carry out, it displays the main menu again and awaits further instructions. This is based on the 'see_rosa_run' variable. This variable should never change. If it does, the program exits and gives the system an error code.
see_rosa_run = True
worsecli.show_main_menu()
while see_rosa_run is True:
    try:
        worsecli.ask_for_input()
    except Exception as e:
        print (e)
        print ()
        print (e.__traceback__)
        input()
else:
    sys.exit(1)
