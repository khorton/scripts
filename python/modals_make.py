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

year = '2015'

conf = """
# Set window title
*.title = Create Modals Line for RV-8 Web Site

# Introductory text
txt.type = text
txt.default = This dialog creates a {modals} line to paste into an article \
on the RV-8 web site in Joomla.
txt.height = 100
txt.width = 310
txt.x = 340
txt.y = 44
txt.tooltip = This is an element of type “text”

# Add a filesystem browser
ob.type = openbrowser
ob.label = Select full size image
ob.width=310
#ob.tooltip = This is an element of type “openbrowser”

# Add a text field
tf.type = textfield
tf.label = Image caption
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
# pop.type = popup
# pop.label = Example popup menu
# pop.width = 310
# pop.option = Popup menu item #1
# pop.option = Popup menu item #2
# pop.option = Popup menu item #3
# pop.default = Popup menu item #2
# pop.tooltip = This is an element of type “popup”

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

caption=result['tf']
if caption == '':
    print('Caption is blank')
    modal_line = '{modal images/' + year + '/' + dirname + '/' + image_file + '|width=2000|height=1333|group=mygallery-' + dirname + '}<img style="margin: 0px 5px 5px 0px; float: left;" src="images/' + year + '/' + dirname + '/thumbs/' + image_comps[0] + '.thumb' + image_comps[1] + '" />{/modal}'
    
else:
    modal_line = '{modal images/' + year + '/' + dirname + '/' + image_file + '|width=2000|height=1333|title=' + caption + '|group=mygallery-' + dirname + '}<img style="margin: 0px 5px 5px 0px; float: left;" src="images/' + year + '/' + dirname + '/thumbs/' + image_comps[0] + '.thumb' + image_comps[1] + '" alt="' + caption +'" />{/modal}'
    # print("Caption is", caption)

print(modal_line)

