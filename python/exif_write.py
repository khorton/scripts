#! /sw/bin/python2.7
# -*- coding: latin-1 -*-

import argparse

parser = argparse.ArgumentParser(description='Update JPGs using exiftool.')
parser.add_argument('-l', dest='latlong', 
  help='optional latitude and longitude, in format "lat, long", with N latitude positive, and E longitude positive')
parser.add_argument('-t', dest='time_delta',
  help='apply time_delta to camera time when comparing against GPS log. Format "+H:MM:SS"')
parser.add_argument('JPGs', nargs='*', default="*.JPGs", 
  help='List of JPG files to process')

args = parser.parse_args()
print(args)


if args.latlong: 
	print "latlong =", args.latlong
	lat,long = args.latlong.split(",")
	lat = float(lat)
	long = float(long)
	if lat>0:
		NS="N"
	else:
		lat*=-1
		NS="S"

	if long>0:
		EW="E"
	else:
		long*=-1
		EW="W"
	# print "lat=%s %s" % (lat,NS)
	# print "long=%s %s" % (long, EW)

	command = "exiftool −overwrite_original_in_place -P -GPSMapDatum=WGS-84 -gps:GPSLatitude=%s -gps:GPSLatitudeRef=%s -gps:GPSLongitude=%s -gps:GPSLongitudeRef=%s -xmp:GPSLatitude='%s %s' -xmp:GPSLongitude='%s %s' -xmp:GPSMapDatum='WGS-84' -xmp:GPSVersionID='2.2.0.0' %s" % (lat, NS, long, EW, lat, NS, long, EW, " ".join(args.JPGs))
	print command
else:
	print "latLong not defined"