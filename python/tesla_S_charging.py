#! /usr/bin/env python3

"""
Tesla Model S Charging Time Calculator
"""

def charge_rate(SOC, charger_max_rate = 250):
	"""
	Return charge rate for a given SOC
	"""
	
	charge_curve = [(0,125),
                  (.10,250),
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
	              (1,    2),   # based on one charge on 2021-01-30
	              (2,    2)]   # to avoid loop going past end of list

# 	charge_curve = [(0,125),
#                   (.10,250),
# 	              (.35,250),
# 	              (.40,213),
# 	              (.45,179),
# 	              (.50,174),
# 	              (.60,130),
# 	              (.70, 95),
# 	              (.80, 71),
# 	              (.85, 64),
# 	              (.90, 54),   # WAG
# 	              (.98, 10),   # based on one charge on 2021-01-30
# 	              (.99,  9),   # based on one charge on 2021-01-30
# 	              (.995, 3.5), # based on one charge on 2021-01-30
# 	              (1,    2),   # based on one charge on 2021-01-30
# 	              (2,    2)]   # to avoid loop going past end of list

	n = 1
	while n <= len(charge_curve) + 1:
		if SOC <= charge_curve[n][0]:
			SOC0 =  charge_curve[n-1][0]
			rate0 = charge_curve[n-1][1]
			SOC1 =  charge_curve[n][0]
			rate1 = charge_curve[n][1]
			rate = rate0 + (rate1 - rate0) * (SOC - SOC0) / (SOC1 - SOC0)
			return min(rate, charger_max_rate)
		else:
			n += 1
		
def charge_time(SOC_start, SOC_end, charger_max_rate=250, ramp_time=30, battery_max_capacity=98):
	"""
	Return time to charge for given SOC_start, SOC_end.
	charger_max_rate defaults to 250 kW and
	ramp_time defaults to 60s to ramp from 0 to initial charge rate
	battery_max_capacity defaults to 98 kWh
	"""
	step_time = 6 # seconds for each step in calculation
	SOC = SOC_start
	duration = 0
	rate = charge_rate(SOC_start, charger_max_rate = charger_max_rate)
	
	# calculate SOC change during ramp up
	SOC += rate / 2 * ramp_time / 3600 / battery_max_capacity
	duration += ramp_time
	
	while SOC < SOC_end:
		SOC_mid_step = SOC + rate / 2 * step_time / 3600 / battery_max_capacity
		rate = charge_rate(SOC_mid_step, charger_max_rate = charger_max_rate)
		SOC += rate * step_time / 3600 / battery_max_capacity
		duration += step_time
	
	return duration / 60

def charge_matrix(charger_max_rate=250,ramp_time=30, battery_max_capacity=98):
	"""
	Print matrix of charge times
	charger_max_rate defaults to 250 kW and
	ramp_time defaults to 60s to ramp from 0 to initial charge rate
	battery_max_capacity defaults to 98 kWh
	output must be either "md" or "latex".  Defaults to "md"
	"""
	SOC_starts = [.05, .1, .15, .2, .3, .4, .5, .6, .7, .8, .9]
	SOC_ends = [.4, .5, .55, .6, .65,  .7, .75, .8, .85, .9, .95, 1]

	print("| Final SOC |  5%  |  10% |  15% |  20% |  30% |  40% |  50% |  60% |  70% |  80% |  90% |")
	print("|-----------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|")

	for SOC_end in SOC_ends:
		line_out = "| {:6,.0f}%   |".format(SOC_end * 100)
		for SOC_start in SOC_starts:
			if SOC_start >= SOC_end:
				next
			duration = charge_time(SOC_start, SOC_end, charger_max_rate=charger_max_rate, ramp_time=ramp_time, battery_max_capacity=battery_max_capacity)
			if SOC_start >= SOC_end:
				line_out += "      |"
			else:
				line_out += "{:5,.0f} |".format(duration)
		print(line_out)
	print("*[2022 Tesla Model S Charge Time vs Start and Final SOC - {:3,.0f} kW Charger]*".format(charger_max_rate))
		
def charge_matrix_latex(charger_max_rates=[250],ramp_time=30, battery_max_capacity=98):
	"""
	Print matrix of charge times
	charger_max_rate defaults to 250 kW and
	ramp_time defaults to 60s to ramp from 0 to initial charge rate
	battery_max_capacity defaults to 98 kWh
	output must be either "md" or "latex".  Defaults to "md"
	"""
	SOC_starts = [.05, .1, .15, .2, .3, .4, .5, .6, .7, .8, .9, ]
# 	SOC_ends = [.3, .4, .5, .55, .6, .65,  .7, .75, .8, .85, .9, .95, 1]
	SOC_ends = [.4, .5, .55, .6, .65,  .7, .75, .8, .85, .9, .95, 1]

	preamble = r"""% !TEX TS-program = pdftex
% !TEX encoding = UTF-8 Unicode


\documentclass[11pt,letterpaper,english]{article}
\usepackage{tabulary}
\usepackage[text={7in,10in},centering]{geometry}
\begin{document}"""

	print(preamble)

	for n, charger_max_rate in enumerate(charger_max_rates):

		if n >= 1:
			print(r'\vspace{0.5 in}')

		table_start = r"""
		\setlength{\tymax}{0.5\linewidth}
		\centering
		\small
		\begin{tabulary}{\textwidth}{|C|C|C|C|C|C|C|C|C|C|C|C|} 
		\hline
		\multicolumn{12}{|c|}{ 2022 Tesla Model S Charging Time (minutes) --"""
		table_start2 = "{:2,.0f} kW Charger".format(charger_max_rate)
		table_start3 = r"""}\\
		\hline
		 Final &\multicolumn{11}{c|}{ Starting SOC }\\
		\cline{2-12}
		 SOC """
		for SOC_start in SOC_starts:
			table_start3 += '& {:3,.0f}\% '.format(SOC_start * 100)
		
		table_start4 = r"""\\
		\hline"""
		print(table_start, table_start2, table_start3, table_start4)

		for SOC_end in SOC_ends:
			line_out = "{:3,.0f}\% ".format(SOC_end * 100)
			for SOC_start in SOC_starts:
				if SOC_start >= SOC_end:
					next
				duration = charge_time(SOC_start, SOC_end, charger_max_rate=charger_max_rate, ramp_time=ramp_time, battery_max_capacity=battery_max_capacity)
				if SOC_start >= SOC_end:
					line_out += "&       "
				else:
					line_out += "& {:5,.0f} ".format(duration)
			line_out += r' \\'
			print(line_out)
			print(r'\hline')
		table_end = r"""
	\end{tabulary}
	"""
		print(table_end)

	print(r'\end{document}')