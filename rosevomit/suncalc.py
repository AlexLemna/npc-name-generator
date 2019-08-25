from decimal import Decimal  # to handle some floating-point messiness
from math import cos, sin, tan, acos, asin, atan2
from math import degrees, radians  # for converting

# Calculating the position of the sun in Earth's sky is weird and kinda mind-bending. The terminology and equations we use for tracking things moving across the sky have been developed over hundreds (thousands?) of years, and they've improved along with our understanding of the universe, but we still have to switch between a few different paradigms while we're doing this. Professional astronomers and experienced amateurs might be able to hold all these interrelated concepts in their head, but me? I compensate by using lots of notes.
# There are three different coordinate systems we need to switch between. We use ecliptic coordinates (technically, geocentric ecliptic coordinates) to calculate the motion of the bodies in the Antikytheran solar system (or, technically, the apparent motion of the sun with respect to Antikythera). The 'ecliptic' that the coordinate system is based on refers to the plane of Antikythera's average orbit around its sun.
# We use equatorial coordinates to talk about *all* of the sky as seen from *all* of Antikythera. Most star charts use equatorial coordinates, and there are fancy telescope mounts that will track a set of equtorial coordinates across the night sky. These coordinates are based on the location of a celestial body relative to where Antikythera's own equator would be if it were projected onto the sky. The equatorial coordinates of stars doesn't change over time (much). The equatorial coordinates of the Sun and the planets will change over time.
#
# I make some simplifications in Antikythera's system. First, the real orbit *is* the average orbit. Deviations from the average orbit are fixed by the unseen "Silent Cosmic Bureaucracy's Conference on Weights and Measures' Department of Continuity Physics' Enforcement Bureau's Orbital Mechanics Division," often abbreviated to CoWMDoCPEB-OrbMech. Second, Antikythera's orbit is perfectly circular and is completed in exactly 365 days (with each day, or rotation of Antikythera arounds its axis, lasting exactly 24 hours.)


def angle_sanity_check (ARG_angle_value):
    """Ensures that a given angle is between 0 and 360 degrees. If the angle is not within that range, it converts it into that range and returns the corrected angle measurement."""
    # First, we need to prevent some floating point messiness by using the decimal module, otherwise we get results like "-750.8 + 360 = -390.79999999999995", which is obviously ever-so-slightly off. Now, we COULD just admit that this is a tiny error that won't be meaningful for our program and automatically round our results to an acceptable level of precision before this function returns the result, but... I'm new to programming, so I still have the energy and inexperience required to be offended by binary floating-point.
    valid_types_for_Decimal_class = [Decimal, str, int, tuple]
    if type (ARG_angle_value) in valid_types_for_Decimal_class:
        angle_value = ARG_angle_value
    else:
        angle_value = str(ARG_angle_value)
    angle_value = Decimal (angle_value)
    # Next, we need to make sure that our angle's measurement is between 0 and 360 degrees. If it's not, we need to convert it to an angle in that range.
    if 0 <= angle_value < 360:
        pass
    else:
        # NOTE: The % operator is the 'modulo' operator
        angle_value = angle_value % 360
        if angle_value < 0:
            angle_value = angle_value + 360
    return angle_value


def TEST_angle_sanity_check():
    # TODO: Move this to tests file.
    angles_to_test = [120, 350, -35, -750.8, 1090, 3601]
    for angle in angles_to_test:
        sane_angle = angle_sanity_check(angle)
        print (f"The sane value of {angle} is {sane_angle}.")


def defaultsiteprompt() -> bool:  # type: ignore, because otherwise mypy seems to want an explicit return statement in the 'else' section
    """Ask for latitude and longitude"""
    print ("The default site for this calculation is Cordu.")
    userinput: str = input ("Enter nothing or [Y] to accept this site, or [N] to input custom coordinates. ")
    if userinput == "Y" or userinput == "y" or userinput == "":
        return True
    elif userinput == "N" or userinput == "n":
        return False
    else:
        print (f"{userinput} is not a valid input. Please enter Y or N.")
        defaultsiteprompt ()


def antikythera_rotation_angle (seconds_elapsed):
    """Returns the 'Antikythera Rotation Angle', equivalent to Earth's 'Earth Rotation Angle' and similar to Earth's 'Greenwich Sidereal Time', though Earth's GST includes an adjustment for the procession of Earth's March equinox that is irrelevant for Antikythera."""
    # validating
    if 0 <= seconds_elapsed <= 86400:
        pass
    else:
        raise ValueError
    # calculating current rotation angle
    hours_elapsed = seconds_elapsed / 3600
    rotation_angle = hours_elapsed * 15
    rotation_angle = angle_sanity_check (rotation_angle)
    return rotation_angle


def solar_hour_angle():
    """Returns the current solar hour angle. The solar hour angle is an expression of time, expressed in angular measurement (degrees), from solar noon. Time before solar noon is measured as negative degrees, and time after solar noon is measured as positive degrees.

    The sun moves at 15 degrees per hour.
    """

# defaults
AXIAL_TILT: float = 27.5
ecliptic_longitude: float
ecliptic_latitude: float
OBLIQUITY_OF_THE_ECLIPTIC: float = AXIAL_TILT
right_ascension: float
declination: float
hour_angle: float
altitude: float
azimuth: float

day: float = 1
dayfrom0: float = day - 1
orbitaldaynumber = O_D_N = dayfrom0

# Main program begins
usedefaults: bool = defaultsiteprompt()
if usedefaults is True:
    LATITUDE = -75.0
    LONGITUDE = -70.0
else:
    LATITUDE = float (input ("What is the latitude? "))
    LONGITUDE = float (input ("What is the longitude? "))

# first, we need to calculate the position of the sun in the ecliptic coordinate system
λ = ecliptic_longitude = dayfrom0 * (360 / 365)
β = ecliptic_latitude = 0

# next, we need to convert the ecliptic coordinates into equitorial coordinates
ϵ = AXIAL_TILT = OBLIQUITY_OF_THE_ECLIPTIC
α = right_ascension = atan2 (cos(ϵ) * sin(λ), cos(λ))
δ = declination = asin (sin(ϵ) * sin(λ))
h = hour_angle = antikythera_rotation_angle(O_D_N) + LATITUDE - degrees(α)

# finally, we need to convert the ecliptic coordinates into horizontal coordinates
part1 = (-sin(LATITUDE) * cos(δ) * cos(h)) + (cos(LATITUDE) * sin(δ))
part2 = cos(δ) * sin(h)
A = azimuth = -atan2(part1, part2)
a = altitude = asin ((sin(LATITUDE) * sin(δ)) + (cos(LATITUDE) * cos(δ) * cos(h)))

A = degrees(A)
a = degrees(a)
zenith: float = 90 - a

print (f"The sun's azimuth is {A} degrees.")
print (f"The sun's altitude is {a} degrees.")
print (f"The sun's angle from the zenith is {zenith} degrees.")
