#! /usr/bin/env python
"""Export Geeklog CMS database to CSV, after twiddling image tags to make them 
compatible with Joomla's image storage location, and the NoNumber Modal
image pop-up extension.
"""

###############################################################################
#                   
# To Do:
#  1. Insert publication date as first para in body, as the Content Uploader
#     extension does not import publication date.
#  2. Write function to extract publication date from body via MySQL calls,
#     and insert in appropriate table.
#  3. Write code to insert Modal class declaration into old GL hard-coded
#     image thumbnail tags.
#  4. Write CSV export function.
#  5. Write input arguement parser.
#
###############################################################################

#mysql python docs at https://github.com/farcepest/MySQLdb1/blob/master/doc/user_guide.rst#mysqldb

import MySQLdb
import sys
import os
import shutil
import csv
import re
from bs4 import BeautifulSoup

base_img_dir='/Library/WebServer/Documents/joomla3/images/'
gl_img_dir='/Users/kwh/temp/joomla3/geeklog-rv8-arvixe/public_html/rv8/images/articles/'
hard_code_gl_img_dir = 'http://www.kilohotel.com/rv8/images/articles/'
joomla_img_dir = 'images/'

db=MySQLdb.connect(user='root',passwd="Yarmouth2",db="rv8_merge")
c=db.cursor()



def parse_all():
    c.execute("SELECT sid, uid, date, title, introtext, bodytext, hits, comments FROM gl_stories")
    story_array = c.fetchmany(2000)
    n = 4
    for row in story_array:
        sid, uid, date, title, introtext, bodytext, hits, comments = row
    
        # get topic id
        c.execute("SELECT tid, id from gl_topic_assignments WHERE id = %s", sid)
        tid, id = c.fetchone()
    
        # get story images, if any
        c.execute("SELECT ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid=%s", id)
        img_array = c.fetchmany(20)
        if c.rownumber > 0:
            print "Story Images:"
            for row in img_array:
                ai_img_num, ai_filename = row
                print ai_img_num, ai_filename
        else:
            print "no images"
    
        print "Story ID=", sid
        # print "ID =", id
        # print "Topic=", tid
        # print "uid=", uid
        print "Story Date/Time=", date
        print "Title=", title
        print "Intro Text=", introtext
        # print "Body Text =", bodytext
        # print "Hits =", hits
    
        soup = BeautifulSoup(introtext,"html5lib")
        print "image html:"
        print soup.find_all('img')
    
        print "Src:", soup.img['src']
        print "Width:", soup.img['width']
        print "Height:", soup.img['height']
        print "Alignment:", soup.img['align']
        print "Alt Text:", soup.img['alt']
        print "==============================\n=============================="
        # Typical pattern if image is hardcoded:
        # <img width="300" height="132" align="right" src="http://www.kilohotel.com/rv8/images/articles/20030507210918708_1.jpg" alt="">


        n -= 1
        if n < 1:
            sys.exit()


def parse_one(sid):
    c.execute("SELECT sid, uid, date, title, introtext, bodytext, hits, comments FROM gl_stories WHERE sid=%s", sid)
    sid, uid, date, title, introtext, bodytext, hits, comments = c.fetchone()

    # get topic id
    c.execute("SELECT tid, id from gl_topic_assignments WHERE id = %s", sid)
    tid, id = c.fetchone()

    # get story images, if any
    c.execute("SELECT ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid=%s", id)
    img_array = c.fetchmany(20)
    imgs=[]
    img_nums=[]
    img_alts=[]
    if c.rownumber > 0:
        print "Story Images:"
        for row in img_array:
            ai_img_num, ai_filename = row
            print ai_img_num, ai_filename
            imgs.append(ai_filename)
            img_nums.append(ai_img_num)
    else:
        print "no images"

    print "Story ID=", sid
    # print "ID =", id
    # print "Topic=", tid
    # print "uid=", uid
    print "Story Date/Time=", date
    print "Short Date=", sid[:8]
    print "Title=", title
    # print "Intro Text=", introtext
    # print "Body Text =", bodytext
    # print "Hits =", hits

    soup = BeautifulSoup(introtext,"html5lib")

    print soup.find_all('img')
    if len(soup.find_all('img')) > 0:
        print "image html atributes:"
        print "Src:", soup.img['src']
        print "Width:", soup.img['width']
        print "Height:", soup.img['height']
        print "Alignment:", soup.img['align']
        print "Alt Text:", soup.img['alt']
    else:
        print "No <img> tags in this article."
        # print soup.find_all(p=re.compile("\[image\d*\]|\[image\d*_left\]|\[image\d*_right\]"))
        # print soup.find_all('p', text=re.compile(".*image.*"))
        # print soup.p(text="image")
        # print soup.p()
        print soup.find_all('p')

    p = new_p(introtext, sid[:8], imgs, img_nums)
    print p
    print "==============================\n=============================="
    # Typical pattern if image is hardcoded:
    # <img width="300" height="132" align="right" src="http://www.kilohotel.com/rv8/images/articles/20030507210918708_1.jpg" alt="">
    
    # output of BeautifulSoup html5 parser (other parsers fail due to missing </img> tag):
    # <img align="right" alt="" height="132" src="http://www.kilohotel.com/rv8/images/articles/20030507210918708_1.jpg" width="300"/>


def new_p(p, date, imgs, img_nums):
    """move images to required directories, and create new <p> in format required by Joomla with modal extension
    convert the image tags from Geeklog [image1_left] to Joomla + Modal extension tags
    convert hard coded paths from Geeklog image directory to Joomla image directory
    
    Notes:
    1. Articles published prior to 08 Jan 2005 had hard coded images in the html, with no thumbnails.
    2. Articles published from 08 Jan 2005 to 13 Oct 2014 have hard coded images, with thumbnails
    3. Articles published after 13 Oct 2014 have [image1_left] tags, and the images listed in the database
    
    return the converted html text block"""

    # sample hard coded image with thumbnail <a href="images/20141013153858942_2_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="images/20141013153858942_2.jpg" alt=""></a>
    # joomla equivalent <a href="images/20141013/20141013153858942_2.jpg" class="modal" title="View unscaled image"><img style="margin: 5px; float: left;" src="images/20141013/20141013153858942_2.jpg"  alt=""/>
    
    img_codes=[]
    image_dir = base_img_dir + date
    os.mkdir(image_dir, 0o775)
    for n, img_thumb in enumerate(imgs):
        file_name_parts=img_thumb.split('.')
        img = file_name_parts[0] + '_original.' + file_name_parts[1]
        
        joomla_thumb_full_path = base_img_dir + date + '/' + img_thumb
        joomla_thumb = joomla_img_dir + date + '/' + img_thumb
        
        joomla_img_full_path = base_img_dir + date + '/' + img
        joomla_img = joomla_img_dir + date + '/' + img
        
        shutil.copy2(gl_img_dir + img_thumb, joomla_thumb_full_path)
        try:
            shutil.copy2(gl_img_dir + img, joomla_img_full_path)
        except IOError:
            print "***", img, "thumbnail image not present"
            
        geeklog_code_left = '[image' + str(img_nums[n]) + '_left]'
        geeklog_code_right = '[image' + str(img_nums[n]) + '_right]'
        geeklog_code_no_align = '[image' + str(img_nums[n]) + ']'
        
        joomla_code_left='<a href="' + joomla_img + '" class="modal"><img style="margin: 5px; float: left;" src="' + joomla_thumb + '" /></a>'
        joomla_code_right='<a href="' + joomla_img + '" class="modal"><img style="margin: 5px; float: right;" src="' + joomla_thumb + '" /></a>'
        joomla_code_no_align='<a href="' + joomla_img + '" class="modal"><img style="margin: 5px;" src="' + joomla_thumb + '" /></a>'
        
        joomla_img_path = joomla_img_dir + date + "/"
        p=p.replace(geeklog_code_left, joomla_code_left)
        p=p.replace(geeklog_code_right, joomla_code_right)
        p=p.replace(geeklog_code_no_align, joomla_code_no_align)
        p=p.replace(hard_code_gl_img_dir, joomla_img_path)
    
    # except Exception as inst:
    #     print type(inst)     # the exception instance
    #     print inst           # __str__ allows args to be printed directly

    return p
    

# parse_all()
# parse_one(20141216012305720) # new article
# parse_one(20030507210918708) # old article with images in Geelog format
# parse_one(2002102621491281) # very first article, with hard coded images
parse_one(20141013153858942) #  sample with hard coded images and thumbnails
