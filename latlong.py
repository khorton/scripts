#! /sw/bin/python2.7

# Script takes lat,long from google maps, and returns it in a format suitable 
# for input into Andrew Turner's iPhoto Geotagging script.
# http://highearthorbit.com/289/
# http://highearthorbit.com/projects/applescript/iPhotoExif.zip

import sys

data_in = sys.argv[1]
lat, lon = data_in.split(',')

lat = float(lat)
lon = float(lon)
# print lat, lon

if lat < 0:
    NS = 'S'
    lat *= -1
else:
    NS = 'N'

if lon < 0:
    EW = 'W'
    lon *= -1
else:
    EW = 'E'

# lat_deg, lat_dec = lat.split('.')
lat_deg = int(lat)
lat_dec = lat - lat_deg
lat_minf = lat_dec * 60
lat_min = int(lat_minf)
lat_sec = (lat_minf - lat_min) * 60

lat_text = "%i deg %i' %5.2f\" %s" % (lat_deg, lat_min, lat_sec, NS)
lat_text2 = "%i,%i,%.2f" % (lat_deg, lat_min, lat_sec)

# print lat_text
print lat_text2

long_deg = int(lon)
long_dec = lon - long_deg
long_minf = long_dec * 60
long_min = int(long_minf)
long_sec = (long_minf - long_min) * 60

long_text = "%i deg %i' %5.2f\" %s" % (long_deg, long_min, long_sec, EW)
long_text2 = "%i,%i,%.2f" % (long_deg, long_min, long_sec)
# print long_text
print long_text2

