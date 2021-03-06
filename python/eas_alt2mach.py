#! /sw/bin/python2.7

"""Return Mach given EAS and Pressure Altitude"""

import airspeed
import argparse

parser = argparse.ArgumentParser(description='Return EAS for a given Mach and pressure altitude')
parser.add_argument('EAS', type=float, 
                    help='Equivalent airspeed')
parser.add_argument('HP', type=float, 
                    help='Pressure Altitude')
parser.add_argument('--speed_units', required=False, default='kt',
                    help='airspeed units - one of "kt", "mph", "km/h", "ft/s" or "m/s".  Defaults to "kt".')
parser.add_argument('--alt_units', required=False, default='ft',
                    help='altitude units - one of feet ("ft"), metres ("m"), kilometres ("km"), statute miles, ("sm") or nautical miles ("nm").  Defaults to "ft".')


args = parser.parse_args()
CAS=airspeed.eas2cas(args.EAS, args.HP, speed_units=args.speed_units, alt_units=args.alt_units)
print(airspeed.cas_alt2mach(CAS, args.HP, speed_units=args.speed_units, alt_units=args.alt_units))