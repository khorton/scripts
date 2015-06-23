#! /usr/bin/env python

"""
create exiftool command line using as input the lat, long from Google Maps 
"What's here".
"""

import sys, os

usage = """
create exiftool command line using as input the lat, long from Google Maps 
"What's here".

In Google Maps, right click on the location of interest.  Select the "What's Here"
option.  Copy the resulting lat, long and paste as the first argument to this script.

Optionally, add file(s) as the second arguement.  If a file list is added, the 
script will run the required exiftool command.

If no files are added, the script will output the exiftool command.  Copy this 
output and manually add the files arquement."""

if len(sys.argv) < 3:
    print usage
    exit()


lat = sys.argv[1]

longg = sys.argv[2]
files = sys.argv[3:]

if lat[-1] == ",":
    lat = lat[:-1]
    
# latsigned = lat

if lat[0] == "-":
    latNS = "S"
    latsigned = lat
    lat = lat[1:]
else:
    latNS = "N"
    

if longg[-1] == ",":
    longg = longg[:-1]

# longsigned = longg
    
if longg[0] == "-":
    longEW = "W"
    longg = longg[1:]
else:
    longEW = "E"

# print latNS, lat
# print longEW, longg
# print files

c1 = "exiftool -overwrite_original_in_place -P -GPSMapDatum=WGS-84 -gps:GPSLatitude="
c2 = " -gps:GPSLatitudeRef="
c3 = " -gps:GPSLongitude="
c4 = " -gps:GPSLongitudeRef="
c5 = " -xmp:GPSLatitude='"
c6 = "'  -xmp:GPSLongitude='"
c7 = "' -xmp:GPSMapDatum='WGS-84' -xmp:GPSVersionID='2.2.0.0'"

command = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (c1, lat, c2, latNS, c3, longg, c4, longEW, c5, lat, latNS, c6, longg, longEW, c7)

if files:
    print "found files"
    print files
    os.execv(command, files)
else:
    command2 = "%s *.(jpg|JPG|arw|ARW)" % command
    print command2
    

