#! /sw/bin/python

import sys

IN = sys.argv[1]

latitude, longitude = IN.split(",")
latitude = float(latitude)
longitude = float(longitude)
# print latitude, longitude

def lms(val_in):
	val_deg = int(val_in)
	val_mn_f = float(val_in - val_deg) * 60
	val_mn = int(val_mn_f)
	val_sec_f = float(val_mn_f - val_mn) * 60
	val_sec = int(val_sec_f)
	return "%i,%i,%i" % (val_deg, val_mn, val_sec)

# print lms(latitude), lms(longitude)

print "%f:%f:0" % (latitude, longitude)