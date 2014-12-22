#! /sw/bin/python2.7
# print Greely SunRise and SunSet times

import ephem as E
gr=E.Observer()
gr.lat, gr.long = '45.252833','-75.582127'
gr.elevation = 110
sun = E.Sun()
  
gr.date = E.Date('2014/11/30')
print "   Date      SunRise    SunSet     HrsUp  Change"
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
  print "%s  %s  %s %s%s" % (rise_text, set_text, up_text, sign, chge_text)
  # print E.localtime(dr).strftime('%d %b %Y %H:%M:%S'), E.localtime(ds).strftime('%H:%M:%S')
  gr.date += 1