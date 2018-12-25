#! /opt/local/bin/python2.7
# print 6621 Rd E.2 NE, Moses Lake SunRise and SunSet times

import ephem as E
ml=E.Observer()
#ml.lat, ml.long = '47.185188','-119.382082' # 6621 Road E.2 NE location
ml.lat, ml.long = '47.2086666','-119.3191666' # KMWH location
ml.elevation = 362 # KMWH elevation 1189 ft
sun = E.Sun()
  
ml.date = E.Date('2018/10/15')
#print "6621 Road E.2 NE Sunrise and Sunset Times\n"
print ("KMWH Sunrise and Sunset Times\n")
print ("   Date      SunRise    SunSet     HrsUp   Change")
upp = 0.
for n in range(415):
  dr = ml.next_rising(sun)
#  azr = ml.sun.rise_az
  ds = ml.next_setting(sun)
#  azs = ml.sun.set_az
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
  ml.date += 1
