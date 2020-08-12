#!/opt/local/bin/python2.7
#-*- coding: utf-8 -*-

#
# USAGE INFORMATION:
# This script inserts IPTC:Caption-Abstract into photos, so that this info
# shows up as the image Description in Apple Photos.
##
# Assumptions: 
#
# Requirements:
#   OS X
#   Pashua http://www.bluem.net/en/mac/pashua/
#   exiftool
#

from __future__ import print_function
import Pashua
import os.path
import os
import sys
import subprocess


conf = """
# Set window title
*.title = Set Description in EXIF

# Introductory text
txt.type = text
txt.default = This dialog sets the photo description (caption) into one or more images.
txt.height = 100
txt.width = 310
txt.x = 340
txt.y = 44
txt.tooltip = This is an element of type “text”

# Add a text field
tf.type = textfield
tf.label = Image caption
tf.default = 
tf.width = 310

# Add a filesystem browser
dest.type = openbrowser
dest.label = Select destination images
dest.width=310
#ob.tooltip = This is an element of type “openbrowser”

# Define radiobuttons
# rb.type = radiobutton
# rb.label = Example radiobuttons
# rb.option = Radiobutton item #1
# rb.option = Radiobutton item #2
# rb.option = Radiobutton item #3
# rb.tooltip = This is an element of type “radiobutton”

# Add a popup menu
# pop.type = popup
# pop.label = Example popup menu
# pop.width = 310
# pop.option = Popup menu item #1
# pop.option = Popup menu item #2
# pop.option = Popup menu item #3
# pop.default = Popup menu item #2
# pop.tooltip = This is an element of type “popup”

# Add 2 checkboxes
recursive.rely = -18
recursive.type = checkbox
recursive.label = Change all files in directory, recursively
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

# print("Pashua returned the following dictionary keys and values:")

# for key in result.keys():
#     print("%s = %s" % (key, result[key]))

if result['cb']=='1':
    sys.exit()

caption=result['tf']
dest_image_path = result['dest']

if result['recursive'] == '1':
    
    if os.path.isdir(dest_image_path):
        command = 'exiftool -overwrite_original -r -IPTC:Caption-Abstract="%s" %s' % (caption, dest_image_path)
    else:
        print('ERROR: Must select directory if recursive option is selected')
        sys.exit()
else:
        command = 'exiftool -overwrite_original -IPTC:Caption-Abstract="%s" %s' % (caption, dest_image_path)

# print("Command is: %s" % (command))
os.system(command)

