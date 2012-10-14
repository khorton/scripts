#! /sw/bin/python2.7

import argparse

parser = argparse.ArgumentParser(description='Update JPGs using exiftool.')
parser.add_argument('-l', dest='latlong', 
  help='optional latitude and longitude, in format "lat,long", with N latitude positive, and E longitude positive')
parser.add_argument('-t', dest='time_delta',
  help='apply time_delta to camera time when comparing against GPS log. Format "+H:MM:SS"')
parser.add_argument('JPGs', nargs='+',
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
	print "lat=%s %s" % (lat,NS)
	print "long=%s %s" % (long, EW)
else:
	print "latLong not defined"