#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# USAGE INFORMATION:
# This script creates a {modal} line to insert popup images on Kevin Horton's
# RV-8 web site, using the NoNumber Modals extension on Joomla.
#
# Select the full size image and enter a caption (caption is optional)
#
# Assumptions: 
#   The year is 2015.  The year can be changed in the year variable at the top
#   The full size image width is 2000 and the height is 1333
#
# Requirements:
#   OS X
#   Pashua http://www.bluem.net/en/mac/pashua/
#

from __future__ import print_function
import Pashua
import os.path
import sys
import os

year = '2015'

conf = """
# Set window title
*.title = Edit EXIF Date

# Introductory text
txt.type = text
txt.default = This dialog edits the date and description embedded in the EXIF of one or more images.
txt.height = 100
txt.width = 310
txt.x = 340
txt.y = 44
txt.tooltip = This is an element of type “text”

# Add a filesystem browser
ob.type = openbrowser
ob.label = Select image or directory
ob.width=310
#ob.tooltip = This is an element of type “openbrowser”
# Add 2 checkboxes
recursive.rely = -18
recursive.type = checkbox
recursive.label = Edit EXIF in all files in directory, recursively

# Add a text field
tf.type = textfield
tf.label = Image description
tf.default = 
tf.width = 310
#tf.tooltip = This is an element of type “textfield”

# Define radiobuttons
# rb.type = radiobutton
# rb.label = Example radiobuttons
# rb.option = Radiobutton item #1
# rb.option = Radiobutton item #2
# rb.option = Radiobutton item #3
# rb.tooltip = This is an element of type “radiobutton”

# Add a popup menu
day.type = popup
day.label = Day
day.width = 40
day.option = 1
day.option = 2
day.option = 3
day.option = 4
day.option = 5
day.option = 6
day.option = 7
day.option = 8
day.option = 9
day.option = 10
day.option = 11
day.option = 12
day.option = 13
day.option = 14
day.option = 15
day.option = 16
day.option = 17
day.option = 18
day.option = 19
day.option = 20
day.option = 21
day.option = 22
day.option = 23
day.option = 24
day.option = 25
day.option = 26
day.option = 27
day.option = 28
day.option = 29
day.option = 30
day.option = 31
day.default = 1
day.tooltip = This is an element of type “popup”

# Add a popup menu
month.type = popup
month.label = Month
month.width = 40
month.option = 1
month.option = 2
month.option = 3
month.option = 4
month.option = 5
month.option = 6
month.option = 7
month.option = 8
month.option = 9
month.option = 10
month.option = 11
month.option = 12
month.default = 1
month.tooltip = This is an element of type “popup”

# Add a text field
year.type = textfield
year.label = year
year.default = 2015
year.width = 60
year.tooltip = Enter the year of the photo

# Add 2 checkboxes
# chk.rely = -18
# chk.type = checkbox
# chk.label = Pashua offers checkboxes, too
# chk.tooltip = This is an element of type “checkbox”
# chk.default = 1
# chk2.type = checkbox
# chk2.label = But this one is disabled
# chk2.disabled = 1
# chk2.tooltip = Another element of type “checkbox”

# Add a cancel button with default label
cb.type = cancelbutton
cb.tooltip = This is an element of type “cancelbutton”

db.type = defaultbutton
db.tooltip = This is an element of type “defaultbutton” (which is \
automatically added to each window, if not included in the configuration)

"""

# Set the images' paths relative to Pashua.app's path
# app_bundle = os.path.dirname(os.path.dirname(Pashua.locate_pashua()))
# icon = app_bundle + '/Resources/AppIcon@2.png'
#
# if os.path.exists(icon):
#     # Display Pashua's icon
#     conf += """img.type = image
#                img.x = 435
#                img.y = 248
#                img.maxwidth = 128
#                img.tooltip = This is an element of type 'image'
#                img.path = %s""" % icon
#

result = Pashua.run(conf)

print("Pashua returned the following dictionary keys and values:")

for key in result.keys():
    print("%s = %s" % (key, result[key]))

if result['cb']=='1':
    sys.exit()

image_path = result['ob']
image_file = os.path.basename(image_path)
image_comps = os.path.splitext(image_file)
dirname = os.path.split(os.path.dirname(image_path))[1]
day = result['day']
month = result['month']
year = result['year']

caption=result['tf']
if caption == '':
    if result['recursive'] == '1':
        if os.path.isdir(image_path):
            command = '/usr/local/bin/exiftool −overwrite_original_in_place -r -AllDates="%s:%s:%s 00:00:00" "%s"' % (year, month, day, image_path)
        else:
            print('ERROR: Must select directory if recursive option is selected')
            sys.exit()
    else:
        command = '/usr/local/bin/exiftool −overwrite_original_in_place -AllDates="%s:%s:%s 00:00:00" "%s"' % (year, month, day, image_path)
        print(command)
else:
    if result['recursive'] == '1':
        if os.path.isdir(image_path):
            command = '/usr/local/bin/exiftool −overwrite_original_in_place -r -AllDates="%s:%s:%s 00:00:00" -IPTC:Caption-Abstract="%s" %s' % (year, month, day, caption, image_path)
        else:
            print('ERROR: Must select directory if recursive option is selected')
            sys.exit()
    else:
        command = '/usr/local/bin/exiftool −overwrite_original_in_place -AllDates="%s:%s:%s 00:00:00" -IPTC:Caption-Abstract="%s" %s' % (year, month, day, caption, image_path)

# os.execl('/usr/bin/pbcopy', modal_line)

print(command)
os.system(command)
