#! /sw/bin/python2.7
# print Greely SunRise and SunSet times

import ephem as E
import argparse

parser = argparse.ArgumentParser(description='Calculate sunrise and sunset times for arbitrary locations')
parser.add_argument('name', type=str, help='location name to display in output')
parser.add_argument('latitude', type=float, help='degrees latitude, with north = positive')
parser.add_argument('longitude', type=float, help='degrees longitude, with east = positive')
parser.add_argument('elevation', type=float, help='site elevation in metres')
parser.add_argument('start_date', type=str, help='start date, in format YYYY/MM/DD')
parser.add_argument('num_days', type=int, help='number of days to calculate')
args = parser.parse_args()

gr=E.Observer()
gr.lat, gr.long = str(args.latitude),str(args.longitude)
gr.elevation = args.elevation
sun = E.Sun()
  
# gr.date = E.Date('2015/11/30')
gr.date = E.Date(args.start_date)
print "%s Sunrise and Sunset Times\n" % (args.name)
print "   Date      SunRise    SunSet     HrsUp   Change"
upp = 0.
for n in range(args.num_days):
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
