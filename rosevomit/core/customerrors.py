# Currently a placeholder file


class RosevomitError(Exception):
    """Base class for developer-defined errors in Rosevomit."""
    pass


class rvGenericError(RosevomitError):
    """An exception to be raised when there is no other RosevomitError that fits the situation."""
    pass


class rvRealityError(RosevomitError):
    """These things should not happen."""
    pass


class rvValidationError(RosevomitError):
    """This exception is meant to be raised in situations where a variable's contents are of an expected type, but the variable's contents do not make sense in the wider context of the program.

    For instance, if our program checks the current (Gregorian calendar) date and discovers that today is July 41st, we'd want to raise an InvalidValueError.
    """
    pass
