# ----------------------------------------
# RandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for randomly generating annual events.

import random


def check_volcano():
    """Checks to see if a volcano explodes."""
    _list = []
    _int = random.randint(1, 50000)
    if _int == 1:
        _list.append("...a supervolcano erupted, rated at an 8 on the Volcanic Explosivity Index. The global impact is substantial, and the regional impact is catastrophic.")
    else:
        pass
    _int = random.randint(1, 750)
    if _int == 1:
        _list.append("...a major volcano erupted, rated at an 7 on the Volcanic Explosivity Index and equivalent to the 1815 eruption of Tambora. The global impact is impossible to miss, the regional impact is substantial, and the local impact is catastrophic.")
    else:
        pass
    _int = random.randint(1, 75)
    if _int == 1:
        _list.append("...a major volcano erupted, rated at an 6 on the Volcanic Explosivity Index and equivalent to the 1883 eruption of Krakatoa. The global impact is notable, the regional impact is substantial, and the local impact is catastrophic.")
    else:
        pass
    return _list
