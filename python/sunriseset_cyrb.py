#! /sw/bin/python3.4
# Resolute Bay
# First sunrise of year is 04 Feb
# Sun last sets on 28 Apr
# Next sunset is 14 Aug
# Last sunrise of year is 06 Nov
import ephem as E
rb=E.Observer()
rb.lat, rb.long = '74.7169444444','-94.9694444444' # CYRB locaton
rb.elevation = 68 # CYRB elevation 222 ft
sun = E.Sun()

rb.date = E.Date('2018/01/01')
print ("CYRB Sunrise and Sunset Times\n")
print ("   Date      SunRise    SunSet     HrsUp   Change")
upp = 0.
for n in range(415):
  try:
    dr = E.Date(rb.next_rising(sun) + 2 * E.hour)
  except:
    dr = ""

  try:
    ds = E.Date(rb.next_setting(sun) + 2 * E.hour)
  except:
    ds = ""

  try:
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

  except TypeError:
    up_text = "--------"
    chge_text = "----"
    sign = ""

  try:
    rise_text = E.localtime(dr).strftime('%d %b %Y  %H:%M:%S')
  except AttributeError:
    rise_text = E.localtime(rb.date).strftime('%d %b %Y')
    rise_text += "     None  "
  # rise_az = 
  
  try:
    set_text = E.localtime(ds).strftime('%H:%M:%S')
  except AttributeError:
    set_text = "  None  "

  print ("%s  %s  %s  %s%s" % (rise_text, set_text, up_text, sign, chge_text))
  # print E.localtime(dr).strftime('%d %b %Y %H:%M:%S'), E.localtime(ds).strftime('%H:%M:%S')
  rb.date += 1
