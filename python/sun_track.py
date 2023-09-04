#! /opt/local/bin/python3
# print('2012 Explorers Trail Sun Azimuth and Elevation vs Time for selected date')

import ephem as E
dp=E.Observer()


dp.lat, dp.long = '44.428220', '-87.982371'
dp.elevation = 212 # KGRB elevation
sun = E.Sun()
  
dp.date = E.Date('2023/09/04 10:00')
print("2012 Explorers Trail Sun Elevation and Aximuth vs Time\n")
print("   Date             Elevation  Azimuth")
print("   Time               (deg)     (deg)")
upp = 0.

for n in range(15*60):
	sun.compute(dp)
	az = sun.az * 180 / 3.1415926
	alt = sun.alt * 180 / 3.1415926
# 	print(str(E.localtime(dp.date)), alt, az)
	lt = E.localtime(dp.date)
	print("%i-%02d-%02d %02d:%02d:%02d   %5.1f      %4.1f" % (lt.year, lt.month, lt.day, lt.hour, lt.minute, lt.second, alt, az))

# 	print("%s %4.1f %4.1f" % (E.localtime(dp.date), alt, az))
	dp.date += 1 / (24 * 60)

