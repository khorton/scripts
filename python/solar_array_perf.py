#! /opt/local/bin/python3

"""
Calculate maximum possible solar array performance vs date
"""

from skyfield.api import N,S,E,W, wgs84, load
from math import cos, sin, acos, pi
import pandas as pd
from datetime import datetime
from pytz import timezone
central = timezone('US/Central')
import matplotlib.pyplot as plt
import numpy as np
# from scipy import integrate

ts = load.timescale()
planets = load('de421.bsp')
earth, sun = planets['earth'], planets['sun']

home = earth + wgs84.latlon(44.428220 * N, 87.98237 * W, elevation_m=212) # KGRB elevation

array = pd.DataFrame()
array['azimuth'] = [140, 230]
array['azimuth'] *= pi / 180
array['tilt'] = [90 - 33.7, 90 - 32]
array['tilt'] *= pi / 180
array['panels'] = [11, 19]
array['rated watts per panel'] = 410
array['max watts per panel'] = 349 # max continuous capacity of microinverters
array['rated watts per section'] = array['panels'] * array['rated watts per panel']
array['max watts per section'] = array['panels'] * array['max watts per panel']


def plot_power_vs_time(df, title_text='Solar Array Power vs Time'):
	"""
	Plot solar array max power vs time from start hour to end hour
	"""
	df.plot(x='hour',y='kW', grid='both', ylabel='Solar Array Power (kW)', legend=False, title=title_text)
	plt.show()

def power_vs_time(array, year, month, day, start_hour, end_hour, inc=.1, attenuation=0, timezone='CENT'):
	"""
	Return Pandas Dataframe of solar array max power vs time from start hour to end hour
	"""
	hours = []
	powers = []
	hour = start_hour
	while hour < end_hour:
		hours.append(hour)
		hour += inc
	
	for h in hours:
		minute = int((h - int(h)) * 60)
		powers.append(max_power(year, month, day, int(h), minute, array, attenuation, timezone) / 1000)
	
	columns = ['hour', 'kW']
	power = pd.DataFrame(columns=columns)
	power['hour'] = hours
	power['kW'] = powers
# 	power['integral'] = power.apply(lambda g: integrate.trapezoid(g['kW'], x=g['hour']))
	
	print(power)

	return power

def max_power(year, month, day, hour, minute, array, attenuation=0, timezone='CENT', debug=False):
	"""
	Return theoretical maximum solar array output in watts for a given date and UTC time
	"""
	d = datetime(year, month, day, hour, minute, 0)
	if timezone == 'CENT':
		dt = central.localize(d) # this accounts for Daylight Savings Time
	else:
		dt = d
	
	t = ts.from_datetime(dt)

	hour += minute / 60
	sun_astro = home.at(t).observe(sun)
	app = sun_astro.apparent()
	sun_elevation, sun_azimuth, sun_distance = app.altaz()
	if debug:
		print("Sun Elevation=", sun_elevation, "\nSun Azimuth=", sun_azimuth)
	if sun_elevation.radians < 0:
		return 0
	else:
		array_power = 0
		for index, row in array.iterrows():
			section_incidence = incidence(sun_azimuth.radians, sun_elevation.radians, row['azimuth'], row['tilt'])
			section_power = min(row['rated watts per section'] * incidence_correction(section_incidence) * (1.0 - attenuation), row['max watts per section'])
			if debug:
				print("Panel Incidence=", section_incidence * 180 / pi, "degrees")
				print('Section Power:', section_power)
				print('Panel Power:', section_power / row['panels'])
			array_power += section_power
		return array_power


def power(year, month, day, hour, minute, array, attenuation=0.09, timezone='CENT', debug=False):
	"""
	Return predicted solar array output in watts for a given date and UTC time, accounting for solar attenuation
	"""	
	return max_power(year, month, day, hour, minute, array, attenuation, timezone, debug)

def period_power(start, end, array, inc=5, attenuation=0.09, timezone='CENT', debug=False):
	"""
	Return total energy produced by array over a period
	
	start and end are tuples of (year, month, day, minute)
	
	inc is the length of the integration slices in minutes
	"""
# 	data = np.array
	

def incidence(sun_azimuth, sun_elevation, panel_azimuth, panel_tilt):
	"""
	Return angle between sun and normal to panel - all angles in radians
	"""
	incidence = acos( cos(pi/2 - sun_elevation) * cos(pi/2 - panel_tilt ) + sin(pi/2 - sun_elevation) * sin(pi/2 - panel_tilt ) * cos(panel_azimuth - sun_azimuth))
	
	return incidence
	
def incidence_correction(incidence):
	"""
	Returns correction factor as function of incidence, with angles in radians
	"""
	incidence_deg = incidence * 180 / pi
	if incidence_deg < 40:
		return cos(incidence)
	elif incidence_deg < 60:
		return cos(incidence) * ( 1 - ( incidence_deg - 40 ) / 400 )
	elif incidence_deg < 70:
		return cos(incidence) * ( 0.95 - ( incidence_deg - 60 ) / 100 )
	elif incidence_deg < 90:
		return cos(incidence) * ( 0.85 - ( incidence_deg - 70 ) / 57.14 )
	else:
		return 0
