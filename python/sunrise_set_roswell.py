#! /opt/local/bin/python2.7
# print Roswell, NM SunRise and SunSet times

loc = "WA"
# loc = "NM"

import ephem as E
gr=E.Observer()
gr.lat, gr.long = '33.2998697','-104.5293976'
gr.elevation = 1118.9
sun = E.Sun()
  
gr.date = E.Date('2019/01/01')
print "Roswell Sunrise and Sunset Times\n"
print "   Date      SunRise    SunSet     HrsUp   Change"
upp = 0.
for n in range(415):
  if loc == "NM":
    dr = gr.next_rising(sun)
    ds = gr.next_setting(sun)
  elif loc == "WA":
    dr = E.Date(gr.next_rising(sun) + 1 * E.hour)
    ds = E.Date(gr.next_setting(sun) + 1 * E.hour)
  else:
    print "Unknown location"
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
