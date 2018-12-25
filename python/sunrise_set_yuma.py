#! /opt/local/bin/python2.7
# print Yuma, AZ (KNYL) SunRise and SunSet times

import ephem as E
yuma=E.Observer()
#yuma.lat, yuma.long = '47.185188','-119.382082' # 6621 Road E.2 NE location
yuma.lat, yuma.long = '32.66','-114.61' # KMWH location
yuma.elevation = 65 # KNYL elevation 213 ft
sun = E.Sun()
  
yuma.date = E.Date('2018/10/15')
#print "6621 Road E.2 NE Sunrise and Sunset Times\n"
print ("KNYL (Yuma, AZ) Sunrise and Sunset Times\n")
print ("   Date      SunRise    SunSet     HrsUp   Change")
upp = 0.
for n in range(415):
  dr = yuma.next_rising(sun)
#  azr = yuma.sun.rise_az
  ds = yuma.next_setting(sun)
#  azs = yuma.sun.set_az
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
  print ("%s  %s  %s  %s%s" % (rise_text, set_text, up_text, sign, chge_text))
  # print E.localtime(dr).strftime('%d %b %Y %H:%M:%S'), E.localtime(ds).strftime('%H:%M:%S')
  yuma.date += 1
