"""This file contains constants that will be used throughout Rosevomit."""
import re

SEE_ROSA_RUN: bool = True

### SOME LISTS OF REGEX PATTERNS FOR PARSING USER INPT
REGEXES_YES: list = [
    re.compile(r"^[Y][ES]*$", flags=re.IGNORECASE),
]
REGEXES_NO: list = [
    re.compile(r"^[N][O]*$", flags=re.IGNORECASE),
]
REGEXES_OPT: list = [
    re.compile(r"^[G][IME]*$", flags=re.IGNORECASE),
    re.compile(r"^[M][ORE]*", flags=re.IGNORECASE),
    re.compile(r"^[O][PTIONS]*", flags=re.IGNORECASE),
    re.compile(r"^[G][IME]*\s*[M][ORE]*\s*[O][PTIONS]*$", flags=re.IGNORECASE),
]
# Dear future self,
# Yeah, I just learned about regular expressions. You got a problem with that?
#   Love, Your(past)self
