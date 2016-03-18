#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# USAGE INFORMATION:
# This script creates a merges PDF files, using pdfjam
#
# Assumptions: 
#  The files to be merged have the same name, except for a numerical file
#  suffix 
#   
#
# Requirements:
#   OS X
#   Pashua http://www.bluem.net/en/mac/pashua/
#   pdfjam
#   LaTeX
#   LaTeX pdfpages package

from __future__ import print_function
import Pashua
import os.path
import sys
import os
import re

# year = '2015'

conf = """
# Set window title
*.title = Merge PDF files

# Introductory text
txt.type = text
txt.default = This dialog selects PDF files to be merged, using pdfjam. \
pdfjam is a shell-script front end to the LaTeX 'pdfpages' package.
txt.height = 100
txt.width = 310
txt.x = 340
txt.y = 44
txt.tooltip = This is an element of type “text”

# Add a filesystem browser
ob.type = openbrowser
ob.label = Select one of the PDF files to be merged
ob.width=310
#ob.tooltip = This is an element of type “openbrowser”

# Add a text field
# tf.type = textfield
# tf.label = Image caption
# tf.default =
# tf.width = 310
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

pdf_path = result['ob']
pdf_file = os.path.basename(pdf_path)
pdf_comps = os.path.splitext(pdf_path)
dirname = os.path.split(os.path.dirname(pdf_path))[1]
(pdf_root_name,pdf_ext) = os.path.splitext(pdf_path)


# split main name from suffix numbers
pdf_name = re.split('(.+?)\d+$',pdf_root_name)[1]
print(pdf_name)

in_name = re.sub(' ', '\ ', pdf_name)
print(in_name)


# pdfjam command
command = '/sw/bin/pdfjam --suffix joined --no-landscape --outfile "' + pdf_name + '.pdf" ' + in_name + '*'

# caption=result['tf']
# if caption == '':
#     print('Caption is blank')
#     modal_line = '{modal images/' + year + '/' + dirname + '/' + image_file + '|width=2000|height=1333|group=mygallery-' + dirname + '}<img style="margin: 0px 5px 5px 0px; float: left;" src="images/' + year + '/' + dirname + '/thumbs/' + image_comps[0] + '.thumb' + image_comps[1] + '" />{/modal}'
#
# else:
#     modal_line = '{modal images/' + year + '/' + dirname + '/' + image_file + '|width=2000|height=1333|title=' + caption + '|group=mygallery-' + dirname + '}<img style="margin: 0px 5px 5px 0px; float: left;" src="images/' + year + '/' + dirname + '/thumbs/' + image_comps[0] + '.thumb' + image_comps[1] + '" alt="' + caption +'" />{/modal}'
#     # print("Caption is", caption)

print(pdf_file)

print(pdf_root_name)
print(command)

# os.execl('/usr/bin/pbcopy', modal_line)

outf = os.popen("pbcopy", "w")
outf.write(command)
outf.close()

