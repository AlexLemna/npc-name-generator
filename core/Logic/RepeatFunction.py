# ----------------------------------------
# RepeatFunction.py
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for repeating other functions.


def repeat (x, y):
    for integer in range (0, y):
        x()


def repeat_decrement (x, y):
    for integer in range (0, y):
        x(y)
        y = (y - 1)
