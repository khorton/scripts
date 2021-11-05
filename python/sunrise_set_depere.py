#! /opt/local/bin/python3
# print('2012 Explorers Trail SunRise and SunSet times')

import ephem as E
dp=E.Observer()

loc = "WA"

dp.lat, dp.long = '44.428220', '-87.982371'
dp.elevation = 212 # KGRB elevation
sun = E.Sun()
  
dp.date = E.Date('2021/11/01')
print("2012 Explorers Trail Sunrise and Sunset Times\n")
print("   Date      SunRise    SunSet     HrsUp   Change")
upp = 0.

for n in range(435):
  if loc == "WI":
    dr = dp.next_rising(sun)
    ds = dp.next_setting(sun)
#   elif loc == "ON":
#     dr = E.Date(dp.next_rising(sun) + E.hour)
#     ds = E.Date(dp.next_setting(sun) + E.hour)
  elif loc == "WA":
    dr = E.Date(dp.next_rising(sun) + 2 * E.hour)
    ds = E.Date(dp.next_setting(sun) + 2 * E.hour)
  else:
    print("Unknown location")

  up = (ds - dr)
  if up < 0:
    up += 1
  uph = up * 24
  h = int(uph)
  min = 60 * (uph - h)
  m = int(min)
  s = int(60 * (min - m))
  up_text = '{:2d}:{:02d}:{:02d}'.format(h, m, s)
  
  chge = up - upp
  sign = "+"
  if chge < 0:
    sign = "-"
    chge *= -1
  chgeh = chge * 24
  ch = int(chgeh)
  chgem = 60 * (chgeh - ch)
  cm = int(chgem)
  cs = int(60 * (chgem - cm))
  upp = up
  chge_text = '{:1d}:{:02d}'.format(cm, cs)
  rise_text = E.localtime(dr).strftime('%d %b %Y  %H:%M:%S')
  # rise_az = 
  set_text = E.localtime(ds).strftime('%H:%M:%S')
  print("%s  %s  %s  %s%s" % (rise_text, set_text, up_text, sign, chge_text))
  # print E.localtime(dr).strftime('%d %b %Y %H:%M:%S'), E.localtime(ds).strftime('%H:%M:%S')
  dp.date += 1
