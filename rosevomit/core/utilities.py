# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# utilities.py
# rosevomit.core.utilities
# ___________________________________________________________________
"""For those little code snippets that don't make sense going anywhere else."""
from configparser import NoOptionError, NoSectionError
from decimal import Decimal
from math import degrees, radians, sin, cos, tan, asin, acos, atan2
import os
import sys
import textwrap

from core import settings

# ======================================================================
#                               SYSTEM
# ======================================================================
def CWD_home():
    """Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory"""
    os.chdir (os.path.dirname (sys.argv[0]))


def debugmessage(debugstring: str, **kwargs):
    """If debugging is on, print 'debugstring'. Otherwise, do nothing."""
    try:
        is_debugging_on: bool = settings.show_debug()
    except (NoSectionError, NoOptionError):
        # TODO: When we add a logging module, this exception should definitely be logged.
        is_debugging_on = True
    if is_debugging_on is True:
        print (textwrap.fill (debugstring), **kwargs)
    else:
        pass


def validate_range (x, startvalue, endvalue, raiseEx: bool=True):
    """Check to see if 'x' is between 'startvalue' and 'endvalue' (inclusive)."""
    assert isinstance (raiseEx, bool)
    arguments = [x, startvalue, endvalue]
    for arg in arguments:
        assert isinstance (arg, (int, float, Decimal))
        # We can't compare floats and Decimals directly, so we need to convert to one or the other. Because Decimals are more accurate, we'll convert the floats to Decimals. If we need speed, we'll convert the Decimals to floats instead.
        if isinstance(arg, float):
            arg = Decimal(arg)
    if raiseEx is True:
        if startvalue <= x <= endvalue:
            pass
        else:
            raise ValueError
    else:
        if startvalue <= x <= endvalue:
            return True
        else:
            return False


def repeat (x, y):
    """Repeats x() 'y' times."""
    for integer in range (0, y):
        x()


def setname(ARG_basename, ARG_fileextension: str="txt"):
    """Determines a valid filename for based off a desired 'ARG_basename'. Checks to make sure that _filename is not already in use. If it is, it adds a number on the end of _filename and keeps checking to see if the new _filename is unused, incrementing the number until it finds an unused _filename. """
    _startnum = 1
    _filename = f"{ARG_basename}{_startnum}.{ARG_fileextension}"
    while os.path.isfile (_filename) is True:
        _startnum = _startnum + 1
        _filename = f"{ARG_basename}{_startnum}.{ARG_fileextension}"
    return _filename


# ======================================================================
#                               MATH
# ======================================================================
def deg2rad(x):
    """Converts degrees to radians."""
    return radians(x)


def rad2deg(x):
    """Converts radians to degrees."""
    return degrees(x)


class Angle(Decimal):
    """An angle, measured in degrees."""
    def __init__(self, deg):
        self._measure = Decimal(angle_sanity_check(Decimal(deg)))

    def add(self, x):
        """Add 'x' to the angle. 'x' should be measured in degrees."""
        x = Decimal(f"{x}")
        _measure = self._measure
        _newmeasure = x + _measure
        self._measure = Decimal(angle_sanity_check(_newmeasure))

    @property
    def indegrees(self):
        """Returns the value of the angle in degrees."""
        return self._measure

    @property
    def inradians(self):
        """Returns the value of the angle in radians."""
        return Decimal(radians(self._measure))

    @property
    def sin_indegrees(self):
        """Returns the value of the sine of the angle in degrees."""
        x = Decimal(degrees(Decimal(sin(Decimal(radians(self._measure))))))
        return x

    @property
    def cos_indegrees(self):
        """Returns the value of the cosine of the angle in degrees."""
        x = Decimal(degrees(Decimal(cos(Decimal(radians(self._measure))))))
        return x

    @property
    def tan_indegrees(self):
        """Returns the value of the tangent of the angle in degrees."""
        x = Decimal(degrees(Decimal(tan(Decimal(radians(self._measure))))))
        return x

    @property
    def asin_indegrees(self):
        """Returns the value of the arcsine (the inverse of the sine) of the angle in degrees."""
        x = Decimal(degrees(Decimal(asin(Decimal(radians(self._measure))))))
        return x

    @property
    def acos_indegrees(self):
        """Returns the value of the arccosine (the inverse of the cosine) of the angle in degrees."""
        x = Decimal(degrees(Decimal(acos(Decimal(radians(self._measure))))))
        return x

    @property
    def atan_indegrees(self, y):
        """Returns the value of the arctangent (the inverse of the tangent) of the angle in degrees."""
        y = Decimal(y)
        x = Decimal(degrees(Decimal(atan2(Decimal(radians(self._measure), Decimal(radians(y)))))))
        return x

    @property
    def sin_inradians(self):
        """Returns the value of the sine of the angle in radians."""
        x = Decimal(sin(Decimal(radians(self._measure))))
        return x

    @property
    def cos_inradians(self):
        """Returns the value of the cosine of the angle in radians."""
        x = Decimal(cos(Decimal(radians(self._measure))))
        return x

    @property
    def tan_inradians(self):
        """Returns the value of the tangent of the angle in radians."""
        x = Decimal(tan(Decimal(radians(self._measure))))
        return x

    @property
    def asin_inradians(self):
        """Returns the value of the arcsine (the inverse of the sine) of the angle in radians."""
        x = Decimal(asin(Decimal(radians(self._measure))))
        return x

    @property
    def acos_inradians(self):
        """Returns the value of the arccosine (the inverse of the cosine) of the angle in radians."""
        x = Decimal(acos(Decimal(radians(self._measure))))
        return x

    @property
    def atan_inradians(self, y):
        """Returns the value of the arctangent (the inverse of the tangent) of the angle in radians."""
        y = Decimal(y)
        x = Decimal(atan2(Decimal(radians(self._measure), Decimal(radians(y)))))
        return x


def angle_sanity_check (ARG_angle_value):
    """Ensures that a given angle is between 0 and 360 degrees. If the angle is not within that range, it converts it into that range and returns the corrected angle measurement."""
    # First, we need to prevent some floating point messiness by using the decimal module, otherwise we get results like "-750.8 + 360 = -390.79999999999995", which is obviously ever-so-slightly off. Now, we COULD just admit that this is a tiny error that won't be meaningful for our program and automatically round our results to an acceptable level of precision before this function returns the result, but... I'm new to programming, so I still have the energy and inexperience required to be offended by binary floating-point.
    if isinstance (ARG_angle_value, (Decimal, str, int, tuple)):
        angle_value = Decimal (ARG_angle_value)
    # The official documentation for the Decimal module suggests that float is *not* a valid type to be directly converted into Decimal object, but the FAQ shows examples that seem to contradict this. Additionally, the code in this elif clause seems to work, so... I guess that suggests that the FAQ is correct, and float *is* a valid type? I dunno.
    # See here: https://docs.python.org/3.7/library/decimal.html#decimal-faq
    # This comment was written while using Python 3.7.4. Future releases may clarify/fix this confusion, in which case this elif clause can be removed. (It's also possible that I'm just missing something obvious and it's not a Python problem.)
    elif isinstance (ARG_angle_value, float):
        angle_value = Decimal (ARG_angle_value)
    else:
        angle_value = Decimal (str(ARG_angle_value))
    # Next, we need to make sure that our angle's measurement is between 0 and 360 degrees. If it's not, we need to convert it to an angle in that range.
    if 0 <= angle_value < 360:
        pass
    else:
        # NOTE: The '%' is the 'modulo' operator
        angle_value = angle_value % 360
        if angle_value < 0:
            angle_value = angle_value + 360
    return angle_value
