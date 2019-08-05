# Currently a placeholder file


class RosevomitError(Exception):
    """Base class for developer-defined errors in Rosevomit."""
    pass


class UnexpectedValueError(RosevomitError):
    """This exception is meant to be raised in situations where a variable's contents are of the expected type and might conceptually make sense in the wider context of our program, but nevertheless is not currently handled by our program.

    The situations where you'd raise this exception are a subset of the situations where you'd raise Python's built-in 'NotImplementedError', except that this exception carries the implication that the relevant functionality is not only not implemented but also not planned to be implemented.
    """
    def __init__(self, _variable):
        Exception.__init__(self, "Rosevomit's UnexpectedValueError exception was raised due to the value in".format(_variable))


class InvalidValueError(RosevomitError):
    """This exception is meant to be raised in situations where a variable's contents are of an expected type, but the variable's contents do not make sense in the wider context of the program.

    For instance, if our program checks the current (Gregorian calendar) date and discovers that today is July 41st, we'd want to raise an InvalidValueError.
    """
    pass
