# ----------------------------------------
# RandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosevomit" that contains functions for randomly generating annual events.

import random


def event_output(x):
    if x:  # Check to see if 'log' is not empty or 0.
        x = int(x)
        if x == 1:
            pass
        elif x == 2:
            pass
        else:
            raise ValueError
    else:
        pass


def check_volcano():
    """Checks to see if a volcano explodes. If 'log' equals 1, a csv file is created. If 'log' equals 2, both a csv and a txt file are created."""
    _list = []
    _int = random.randint(1, 50000)
    if _int == 1:
        _list.append("...a SUPERVOLCANO erupted, rated at an 8 on the Volcanic Explosivity Index. The global impact is substantial, and the regional impact is catastrophic.")
    else:
        pass
    _int = random.randint(1, 750)
    if _int == 1:
        _list.append("...a MAJOR VOLCANO erupted, rated at an 7 on the Volcanic Explosivity Index and equivalent to the 1815 eruption of Tambora. The global impact is impossible to miss, the regional impact is substantial, and the local impact is catastrophic.")
    else:
        pass
    _int = random.randint(1, 75)
    if _int == 1:
        _list.append("...a MAJOR VOLCANO erupted, rated at an 6 on the Volcanic Explosivity Index and equivalent to the 1883 eruption of Krakatoa. The global impact is notable, the regional impact is substantial, and the local impact is catastrophic.")
    else:
        pass
    return _list


def check_earthquake():
    """Checks to see if an earthquake occurs. Note that the frequency values here are not exactly based off real-life values. Also note that there are 10 - 20 serious earthquakes (rated X) each year that fall below XI and XII. These are omitted due to their frequency."""
    _list = []
    _int = random.randint(1, 400)
    if _int == 1:
        _list.append("...a CATASTROPHIC EARTHQUAKE occured, rated at an XII on the Modified Mercalli Scale. Very few structures remain standing. All building foundations have been irrepairably damaged. Bridges destroyed. Underground infrastructure and structures destroyed. Waves seen on ground surfaces. Lines of sight and level permanently distorted. Damage total.")
    else:
        pass
    _int = random.randint(1, 50)
    if _int == 1:
        _list.append("...a MAJOR EARTHQUAKE occured, rated at an XI on the Modified Mercalli Scale. Few masonry structures survive - if any. Some well-built wooden structures survive, though none are unscathed. All building foundations have been severely damaged.")
    else:
        pass
    return _list


def check_impact():
    _list = []
    _int = random.randint(1, 440000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 1km wide.")
    else:
        pass
    _int = random.randint(1, 190000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 700m wide.")
    else:
        pass
    _int = random.randint(1, 100000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 400m wide.")
    else:
        pass
    _int = random.randint(1, 73000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 300m wide.")
    else:
        pass
    _int = random.randint(1, 59000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 250m wide.")
    else:
        pass
    _int = random.randint(1, 36000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 200m wide.")
    else:
        pass
    _int = random.randint(1, 16000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 150m wide.")
    else:
        pass
    _int = random.randint(1, 11000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 130m wide.")
    else:
        pass
    _int = random.randint(1, 5200)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 100m wide.")
    else:
        pass
    return _list


def check_astronomy():
    _list = []
    _int = random.randint(1, 300)
    if _int == 1:
        _int = random.randint(1, 4)
        if _int == 1:
            _list.append("...a star suddenly brightened, becoming a SUPERNOVA. It remains visible for many months.")
        else:
            _list.append("...a new star, a SUPERNOVA, became visible. It remains visible for many months.")
    else:
        pass
    return _list
