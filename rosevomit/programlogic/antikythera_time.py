from decimal import Decimal

from core.utilities import validate_range


def time2fractday (day, hour=0, minute=0, second=0):
    arglist = [day, hour, minute, second]
    for arg in arglist:
        if type(arg) is not int: raise TypeError
    validate_range (day, 1, 365, raiseEx=True)
    validate_range (hour, 0, 23, raiseEx=True)
    validate_range (minute, 0, 60, raiseEx=True)
    validate_range (second, 0, 60, raiseEx=True)
    day = day - 1
    _result = day + Decimal(f"{hour / 24}") + Decimal(f"{minute / 1440}") + Decimal(f"{second / 86400}")
    return _result
