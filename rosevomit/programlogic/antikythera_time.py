# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# antikythera_time.py
# rosevomit.programlogic.antikythera_time
# ___________________________________________________________________
"""A file containing functions related to Antikythera's date/time/calendars."""
from decimal import Decimal

from core import logs
from core.utilities import validate_range


_TIMETRACKER = logs.BaseLogger (__name__)


def time2fractday (ARG_day, ARG_hour=0, ARG_minute=0, ARG_second=0):
    """This function accepts arguments for a given time (day, hour, minute, and second) of the year, and returns the equivalent fractional day."""
    arglist = [ARG_day, ARG_hour, ARG_minute, ARG_second]
    for arg in arglist:
        assert isinstance (arg, int)
    validate_range (ARG_day, 1, 365, ARG_raise_ex=True)
    validate_range (ARG_hour, 0, 23, ARG_raise_ex=True)
    validate_range (ARG_minute, 0, 60, ARG_raise_ex=True)
    validate_range (ARG_second, 0, 60, ARG_raise_ex=True)
    # Adjusting the day to a "0th count day"
    day_0_count = ARG_day - 1
    result = day_0_count + Decimal(f"{ARG_hour / 24}") + Decimal(f"{ARG_minute / 1440}") + Decimal(f"{ARG_second / 86400}")
    return result
