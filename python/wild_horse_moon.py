#! /opt/local/bin/python3

"""
Calculate Moon azimuth and elevation for specified location and time
"""

import ephem
import datetime


# moon.compute(wild_horse)
# print('Observer', wild_horse)
# print('AZ', moon.az, 'ELEV', moon.alt)

def output(observer, body, start, time_offset=7,  inc=1, iterations = 60):
	# convert to UTC
	observer.date = start + time_offset * ephem.hour

	for n in range(iterations):
		body.compute(observer)
		print(ephem.localtime(observer.date), body.az, body.alt)
		observer.date += ephem.minute * inc
		
def main():
	day_local = '2020/8/03 21:00:00'
	moon = ephem.Moon()

	wild_horse = ephem.Observer()
	wild_horse.date = day_local
	wild_horse.lat = ephem.degrees('46.968359')
	wild_horse.lon = ephem.degrees('-119.966648')
	wild_horse.elevation = 330

	output(wild_horse, moon, wild_horse.date, inc = 0.5, iterations = 120, time_offset = 7)
	
if __name__ == '__main__':
	main()