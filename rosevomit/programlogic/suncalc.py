# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# suncalc.py
# rosevomit.programlogic.suncalc
# ___________________________________________________________________
# pylint: skip-file
"""A file that contains functions for calculating the position across Antikythera, dependinging on the time and date."""
import csv
from decimal import Decimal
from math import cos, sin, tan, acos, asin, atan2
from math import degrees, radians
from math import pi
import operator
import os
import time

from core import directories
from core.utilities import Angle, deg2rad, rad2deg, angle_sanity_check
from programlogic import antikythera_time

# defaults
AXIAL_TILT = 10  # Note that axial tilt is also called "obliquity of the ecliptic"

def main(lat, long, ARG_output_directory=None, ARG_output_file="results"):
    lat = Decimal(lat)
    long = Decimal(long)
    minute_intervals = [0, 15, 30, 45]
    timed_results = []
    if isinstance (ARG_output_directory, str):
        path = directories.get_dir(ARG_output_directory)
        os.chdir (path)
    # TODO: Move "setname" check from dialogsave.proactive to here!
    with open(f"{ARG_output_file}.txt", mode="w+") as textfile, open(f"{ARG_output_file}.csv", mode="w+") as csvfile:
        textfile.write (f"LATITUDE: {lat} LONGITUDE: {long} \n")
        textfile.write (f"{44 * '-'} \n")
        csvwriter = csv.writer(csvfile, lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
        csvheaders = ["DAY", "HOUR24", "MINUTE", "FRACTIONAL DAY", "DATESTRING", "ALTITUDE", "AZIMUTH"]
        csvwriter.writerow (csvheaders)
        for item in range (1, 366):
            D = item
            textfile.write (f"{15* ' '} AZIMUTH   ALTITUDE  FRACTIONAL DAY\n")
            daily_solar_altitudes = []
            for item in range (0, 24):
                H24 = item
                if H24 < 12:
                    a = "am"
                    H12 = H24
                elif H24 == 12:
                    a = "pm"
                    H12 = H24
                else:
                    a = "pm"
                    H12 = H24 - 12
                for item in minute_intervals:
                    M = item
                    fractday = antikythera_time.time2fractday (D, H24, M)
                    starttime = time.time()
                    (alt, az) = sun_alt_az (fractday, lat, long)
                    endtime = time.time()
                    elapsedtime = endtime - starttime
                    timed_results.append (elapsedtime)
                    # text file writing
                    pretty_az = finalformatting_degrees (az)
                    pretty_alt = finalformatting_degrees (alt)
                    HH = str(H12).zfill(2)
                    MM = str(M).zfill(2)
                    timestamp = (f"{HH}:{MM}{a}")
                    datestring = str((f"Day {D}, {timestamp}"))
                    textfile.write (f"{datestring}  {pretty_az}  {pretty_alt}  {fractday}\n")
                    # quick aside to keep track of local altitudes by timestamps
                    daily_solar_altitudes.append ((timestamp, alt))
                    # csv file writing
                    results = [D, H24, M, fractday, datestring, alt, az]
                    csvwriter.writerow (results)
            local_sunrise, local_sunset = getsunrise_and_sunset (daily_solar_altitudes)
            local_noon = max (daily_solar_altitudes, key=operator.itemgetter(1))[0]
            local_midnight = min (daily_solar_altitudes, key=operator.itemgetter(1))[0]
            local_results_string1 = str(f"Local sunrise: {local_sunrise}  Local sunset: {local_sunset} \n")
            local_results_string2 = str(f"Local noon: {local_noon}  Local midnight: {local_midnight} \n")
            textfile.write (local_results_string1)
            textfile.write (local_results_string2)
            textfile.write ("\n")
            if D is 1:
                print (f"Done with day {D}, ", end="")
            elif 1 < D < 365:
                print (f"{D}, ", end="")
            else:
                print (f"{D}. ", end="")
                avgtime = sum (timed_results) / len (timed_results)
                print (f"Average time per minute interval: {avgtime} seconds")


def antikythera_rotation_angle (astrodate):
    """Returns the 'Antikythera Rotation Angle', equivalent to Earth's 'Earth Rotation Angle' and similar to Earth's 'Greenwich Sidereal Time', though Earth's GST includes an adjustment for the procession of Earth's March equinox that is irrelevant for Antikythera."""
    # validating
    if 0 <= astrodate <= 365:
        pass
    else:
        raise ValueError
    # calculating current rotation angle
    rotation_angle = astrodate * (360 + Decimal(0.9856))
    rotation_angle = angle_sanity_check (rotation_angle)
    # rotation_angle = rotation_angle
    return rotation_angle


def sun_alt_az (fractionalday, latitude, longitude):
    """Expects latitude and longitude in degrees.
    """
    global AXIAL_TILT
    latitude = Angle(latitude)
    longitude = Angle(longitude)
    ϵ = Angle(f"{AXIAL_TILT}")
    julianday = Decimal(f"{fractionalday}") - Decimal("0.5")

    # first, we need to calculate the position of the sun in the ecliptic coordinate system
        # Mean longitude is the ecliptic longitude that an orbiting body could be found at, if its orbit were circular and free of perturbations. Because our orbit actually *is*, our mean longitude actually *does* equal the ecliptic longitude.
        # In a circular orbit, mean longitude = ecliptic longitude.
        # In a circular orbit with 0 inclination, mean anomaly = mean longitude = ecliptic longitude
    ecliptic_longitude = Angle(julianday * Decimal(f"{360 / 365}"))
    λ = ecliptic_longitude
    ecliptic_latitude = Angle(Decimal('0'))
    β = ecliptic_latitude

    # next, we need to convert the ecliptic coordinates into equitorial coordinates
        # ra and declination
    right_ascension = Decimal(atan2 (ϵ.cos_inradians * λ.sin_inradians, λ.cos_inradians))
    declination = Decimal(asin (ϵ.sin_inradians * λ.sin_inradians))
    right_ascension = Angle(rad2deg(right_ascension))
    declination = Angle(rad2deg(declination))
    α = right_ascension
    δ = declination
        # hour angle
    ara = antikythera_rotation_angle (fractionalday)
    ara = Angle(ara)
    hour_angle = (ara.inradians + Decimal(pi)) + latitude.inradians - α.inradians
    h = Angle(rad2deg(hour_angle))

    # finally, we need to convert the ecliptic coordinates into horizontal coordinates
        # azimuth
    part1 = (-latitude.sin_inradians * δ.cos_inradians * h.cos_inradians) + (latitude.cos_inradians * δ.sin_inradians)
    part2 = δ.cos_inradians * h.sin_inradians
    azimuth = Decimal(-atan2(part1, part2))
        # altitude
    altitude = Decimal(asin ((latitude.sin_inradians * δ.sin_inradians) + (latitude.cos_inradians * δ.cos_inradians * h.cos_inradians)))

    azimuth = rad2deg(azimuth)
    altitude = rad2deg(altitude)
    return (altitude, azimuth)


def finalformatting_degrees (x):
    assert isinstance (x, (int, float, Decimal))
    _result = round(x, 2)
    if _result >= 0:
        _sign = "+"
    else:
        _sign = "-"
    _result = abs(_result)  # to remove sign
    _result = float(_result)  # to ensure decimal
    # splitting up so we can measure section length and pad with appropriate spaces
    _part1, _part2 = str(_result).split(".")
    _extra_spaces = (3 - len(_part1)) * " "
    _extra_zeroes = (2 - len(_part2)) * "0"
    _result = _sign + _extra_spaces + _part1 + "." + _part2 + _extra_zeroes + "°"
    return _result


def getsunrise_and_sunset(x):
    """Given a list of tuples in (timestamp: str, altitude: float) format, returns the timestamps of the local sunrise and sunset.
    """
    local_x = x.copy()
    assert isinstance (local_x, list)
    # Get sunrise
    solar_alt_tuple = local_x.pop(0)
    assert isinstance (solar_alt_tuple, tuple)

    sunrise_string = "No sunrise."
    sunset_string = "No sunset"
    if solar_alt_tuple[1] > 0:
        sunrise_string = "Sun already up."
        try:
            while solar_alt_tuple[1] > 0:
                solar_alt_tuple = local_x.pop(0)
            sunset_string = solar_alt_tuple[0]
        except IndexError:
            return sunrise_string, sunset_string
    elif solar_alt_tuple[1] == 0:
        sunrise_string = solar_alt_tuple[0]
        try:
            while solar_alt_tuple[1] > 0:
                solar_alt_tuple = local_x.pop(0)
            sunset_string = solar_alt_tuple[0]
        except IndexError:
            return sunrise_string, sunset_string
    else:
        try:
            while solar_alt_tuple[1] < 0:
                solar_alt_tuple = local_x.pop(0)
            sunrise_string = solar_alt_tuple[0]
            while solar_alt_tuple[1] > 0:
                solar_alt_tuple = local_x.pop(0)
            sunset_string = solar_alt_tuple[0]
        except IndexError:
            return sunrise_string, sunset_string
    return sunrise_string, sunset_string
