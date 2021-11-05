#! /opt/local/bin/python3
# print KGRB SunRise and SunSet times

loc = "WA"
# loc = "WI"

import ephem as E
gb=E.Observer()
gb.lat, gb.long = '44.4846336','-88.1297133'
gb.elevation = 212 # KGRB elevation (m)
sun = E.Sun()
  
gb.date = E.Date('2021/05/01')
print("KGRB Sunrise and Sunset Times\n")
# print "KGRB Sunrise and Sunset Times\n"
print("   Date      SunRise    SunSet     HrsUp   Change")
upp = 0.

for n in range(435):
  if loc == "WI":
    dr = gb.next_rising(sun)
    ds = gb.next_setting(sun)
  elif loc == "WA":
    dr = E.Date(gb.next_rising(sun) + 2 * E.hour)
    ds = E.Date(gb.next_setting(sun) + 2 * E.hour)
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
  gb.date += 1
