"""Various properties from Mars
Author: C. Grima (cyril.grima@gmail.com)
"""

from planetbody.Classdef import Body

nfo = Body('planet',  # category
           'Mars',  # name
           'Martian',  # adjective
           'S IV',  # acronym
           'Sun',  # parent body
           6.4185e23,  # mass [kg]
           {'a':3396.2e3,
            'b':3396.2e3,
            'c':3376.2e3}, # radius [m]
           1.025957,  # rotation [days]
           227939100e3,  # semimajor axis [m]
           249200000e3,  # apoapsis radius [m]
           206700000e3,  # periaspsis radius [m]
           25.19,  # rotation axis tilt [deg]
           1.850,  # orbit plan inclination [deg]
           286.537,  # longitude of the periapsis argument [deg]
           49.562  # Ascending node [deg]
          )