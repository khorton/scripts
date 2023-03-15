#! /usr/bin/env python3

"""
Tesla Model S Charging Time Calculator
"""

def charge_rate(SOC, charger_max_rate = 250):
	"""
	Return charge rate for a given SOC
	"""
	
	charge_curve = [(0,250),
	              (.35,250),
	              (.40,205),
	              (.47,164),
	              (.50,153),
	              (.67,105),
	              (.80, 71),
	              (.88, 55),
	              (.91, 52),
	              (.95, 45),   # WAG
	              (.98, 10),   # based on one charge on 2021-01-30
	              (.99,  7),   # based on one charge on 2021-01-30
	              (.995, 3.5), # based on one charge on 2021-01-30
	              (1,    2)]   # based on one charge on 2021-01-30
	print(type(SOC))
	print(charge_curve[1][0])
	print(type(charge_curve[1][0]))

	if SOC <= charge_curve[0][0]:
		print("loop ", 0, charge_curve[n][1])
		return min(charge_curve[0][1], charger_max_rate)

	elif SOC <= charge_curve[1][0]:
		print("loop ", 1, charge_curve[1][1])
		return min(charge_curve[1][1], charger_max_rate)

	elif SOC <= charge_curve[2][0]:
		print("loop ", 2, charge_curve[2][1])
		return min(charge_curve[2][1], charger_max_rate)

	elif SOC <= charge_curve[3][0]:
		print("loop ", 3, charge_curve[3][1])
		return min(charge_curve[3][1], charger_max_rate)

	elif SOC <= charge_curve[4][0]:
		print("loop ", 4, charge_curve[4][1])
		return min(charge_curve[4][1], charger_max_rate)

	elif SOC <= charge_curve[5][0]:
		print("loop ", 5, charge_curve[5][1])
		return min(charge_curve[5][1], charger_max_rate)

	elif SOC <= charge_curve[6][0]:
		print("loop ", 6, charge_curve[6][1])
		return min(charge_curve[6][1], charger_max_rate)

	elif SOC <= charge_curve[7][0]:
		print("loop ", 7, charge_curve[7][1])
		return min(charge_curve[7][1], charger_max_rate)

	elif SOC <= charge_curve[8][0]:
		print("loop ", 8, charge_curve[8][1])
		return min(charge_curve[8][1], charger_max_rate)

	elif SOC <= charge_curve[9][0]:
		print("loop ", 9, charge_curve[9][1])
		return min(charge_curve[9][1], charger_max_rate)

	else:
		print("at the end")
