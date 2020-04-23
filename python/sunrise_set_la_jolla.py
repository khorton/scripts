
#! /opt/local/bin/python2.7
# print La Jolla, CA SunRise and SunSet times

import ephem as E
gr=E.Observer()
gr.lat, gr.long = '32.850328','-117.272712' # La Jolla, CA location
gr.elevation = 10 # La jolla elevation
sun = E.Sun()
  
gr.date = E.Date('2019/06/10')
# print "6621 Road E.2 NE Sunrise and Sunset Times\n"
print "La Jolla Sunrise and Sunset Times\n"
print "   Date      SunRise    SunSet     HrsUp   Change"
upp = 0.
for n in range(415):
  dr = gr.next_rising(sun)
  ds = gr.next_setting(sun)
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
  set_text = E.localtime(ds).strftime('%H:%M:%S')
  print "%s  %s  %s  %s%s" % (rise_text, set_text, up_text, sign, chge_text)
  # print E.localtime(dr).strftime('%d %b %Y %H:%M:%S'), E.localtime(ds).strftime('%H:%M:%S')
  gr.date += 1
