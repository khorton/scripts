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

"""
from bs4 import BeautifulSoup as BS
import MySQLdb as M
db=M.connect(user='root',passwd="Yarmouth2",db="rv8_merge")
c=db.cursor()
c.execute("SELECT sid, uid, date, title, introtext, bodytext, hits, comments FROM gl_stories WHERE sid=20141013153858942")
sid, uid, date, title, introtext, bodytext, hits, comments = c.fetchone()
introtext
soup = BS(introtext,"html5lib")
soup

DT='***DateTime:2003-07-01 20:58:30'
date_tag=soup.new_tag('p')
date_tag.insert(0,DT)
soup.body.insert(0,date_tag)

dt=soup.p.extract()
DT=dt.string


Introtext, straight from database
<p><br>\r<a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1_original.jpg" title="View unscaled image"><img width="300" height="200" align="left" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg" alt=""></a>The weather on Sunday was wonderful, and we took full advantage by flying to Toronto for lunch. <a href="http://en.wikipedia.org/wiki/Billy_Bishop_Toronto_City_Airport">Toronto City Centre Airport</a> is on an island close to the CN Tower, right next to downtown Toronto. It is the main hub for <a href="http://en.wikipedia.org/wiki/Porter_Airlines">Porter Airlines</a>, and is a great way to get to downtown Toronto. </p>\r\r<p>Here you see downtown Toronto, the CN Tower, and the airport as we approach from the west.<br clear="all"><hr align="center" width="95%"></p>\r\r<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2.jpg" alt=""></a>The view as we turn onto base leg for runway 08.<br clear="all"><hr align="center" width="95%"></p>\r\r<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3.jpg" alt=""></a>Calling Nav Canada to close our flight plan.<br clear="all"><hr align="center" width="95%"></p>\r\r<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4.jpg" alt=""></a>Terry, after a great lunch, ready to head back home.<br clear="all"><hr align="center" width="95%"></p>\r\r<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5.jpg" alt=""></a>The Porter Airlines terminal, and some of their DeHavilland Dash 8 aircraft, seen shortly after take-off.<br clear="all"><hr align="center" width="95%"></p>\r\r<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6.jpg" alt=""></a>The <a href="http://en.wikipedia.org/wiki/Rogers_Centre">Rogers Centre</a> and the <a href="http://en.wikipedia.org/wiki/CN_Tower">CN Tower</a>, off our left, just east of the airport.</p>

whole document, from BeautifulSoup, using html5lib parser:

<html><head></head><body><p><br/>
<a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1_original.jpg" title="View unscaled image"><img align="left" alt="" height="200" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg" width="300"/></a>The weather on Sunday was wonderful, and we took full advantage by flying to Toronto for lunch. <a href="http://en.wikipedia.org/wiki/Billy_Bishop_Toronto_City_Airport">Toronto City Centre Airport</a> is on an island close to the CN Tower, right next to downtown Toronto. It is the main hub for <a href="http://en.wikipedia.org/wiki/Porter_Airlines">Porter Airlines</a>, and is a great way to get to downtown Toronto. </p>

<p>Here you see downtown Toronto, the CN Tower, and the airport as we approach from the west.<br clear="all"/></p><hr align="center" width="95%"/><p></p>

<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2.jpg" width="299"/></a>The view as we turn onto base leg for runway 08.<br clear="all"/></p><hr align="center" width="95%"/><p></p>

<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3.jpg" width="299"/></a>Calling Nav Canada to close our flight plan.<br clear="all"/></p><hr align="center" width="95%"/><p></p>

<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4.jpg" width="299"/></a>Terry, after a great lunch, ready to head back home.<br clear="all"/></p><hr align="center" width="95%"/><p></p>

<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5.jpg" width="299"/></a>The Porter Airlines terminal, and some of their DeHavilland Dash 8 aircraft, seen shortly after take-off.<br clear="all"/></p><hr align="center" width="95%"/><p></p>

<p><a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6.jpg" width="299"/></a>The <a href="http://en.wikipedia.org/wiki/Rogers_Centre">Rogers Centre</a> and the <a href="http://en.wikipedia.org/wiki/CN_Tower">CN Tower</a>, off our left, just east of the airport.</p></body></html>

In [26]: soup('a')
Out[26]: 
[<a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1_original.jpg" title="View unscaled image"><img align="left" alt="" height="200" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg" width="300"/></a>,
 <a href="http://en.wikipedia.org/wiki/Billy_Bishop_Toronto_City_Airport">Toronto City Centre Airport</a>,
 <a href="http://en.wikipedia.org/wiki/Porter_Airlines">Porter Airlines</a>,
 <a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2.jpg" width="299"/></a>,
 <a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3.jpg" width="299"/></a>,
 <a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4.jpg" width="299"/></a>,
 <a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5.jpg" width="299"/></a>,
 <a href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6.jpg" width="299"/></a>,
 <a href="http://en.wikipedia.org/wiki/Rogers_Centre">Rogers Centre</a>,
 <a href="http://en.wikipedia.org/wiki/CN_Tower">CN Tower</a>]

In [27]: for item in soup('a'):
    item['class']='modal'
   ....:     

In [28]: soup('a')
Out[28]: 
[<a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1_original.jpg" title="View unscaled image"><img align="left" alt="" height="200" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg" width="300"/></a>,
 <a class="modal" href="http://en.wikipedia.org/wiki/Billy_Bishop_Toronto_City_Airport">Toronto City Centre Airport</a>,
 <a class="modal" href="http://en.wikipedia.org/wiki/Porter_Airlines">Porter Airlines</a>,
 <a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_2.jpg" width="299"/></a>,
 <a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_3.jpg" width="299"/></a>,
 <a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_4.jpg" width="299"/></a>,
 <a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_5.jpg" width="299"/></a>,
 <a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6_original.jpg" title="View unscaled image"><img align="left" alt="" height="199" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_6.jpg" width="299"/></a>,
 <a class="modal" href="http://en.wikipedia.org/wiki/Rogers_Centre">Rogers Centre</a>,
 <a class="modal" href="http://en.wikipedia.org/wiki/CN_Tower">CN Tower</a>]



In [42]: soup('a')[0]['href']
Out[42]: u'http://www.kilohotel.com/rv8/images/articles/20141013153858942_1_original.jpg'

In [45]: soup('img')[0]
Out[45]: <img align="left" alt="" height="200" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg" width="300"/>

In [46]: soup('img')[0]['src']
Out[46]: u'http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg'

In [47]: soup('img')[0]['alt']
Out[47]: u''

In [48]: soup('img')[0]['width']
Out[48]: u'300'

In [49]: soup('img')[0]['height']
Out[49]: u'200'

In [50]: soup('a')[0]['class']='modal'

In [51]: soup('a')[0]
Out[51]: <a class="modal" href="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1_original.jpg" title="View unscaled image"><img align="left" alt="" height="200" src="http://www.kilohotel.com/rv8/images/articles/20141013153858942_1.jpg" width="300"/></a>

"""

import MySQLdb
import sys
import os
import shutil
import csv
import re
from bs4 import BeautifulSoup
import bs4


base_img_dir='/Library/WebServer/Documents/joomla3/images/'
gl_img_dir='/Users/kwh/temp/joomla3/geeklog-rv8-arvixe/public_html/rv8/images/articles/'
hard_code_gl_img_dir = 'http://www.kilohotel.com/rv8/images/articles/'
hard_code_gl_img_dir2 = 'http://go.phpwebhosting.com/~khorton/rv8/images/articles/'
joomla_img_dir = 'images/'

db=MySQLdb.connect(user='root',passwd="Yarmouth2",db="rv8_merge")
c=db.cursor()

thumbnail=re.compile('.*_original.*')



def parse_all(csv_file_name='/Users/kwh/temp/GL_export.csv'):
    
    # with open(csv_file_name, 'wb') as csvfile:
    #     GLwriter = csv.writer(csvfile)
    csvfile = open(csv_file_name, 'wb') 
    GLwriter = csv.writer(csvfile)
        
    GLwriter.writerow(['Title', 'catid', 'Section', 'introtext', 'fulltext', 'created', 'created_by', 'hits', 'state', 'modified date', 'start publishing', 'finish publishing', 'created_by_alias', 'access', 'featured', 'language', 'alias'])
    
    c.execute("SELECT sid, uid, date, title, introtext, bodytext, hits, comments FROM gl_stories WHERE export_flag=0 limit 1000")
    story_array = c.fetchmany(2000)

    for row in story_array:
        sid, uid, pub_date, title, introtext, bodytext, hits, comments = row
        pub_date = str(pub_date)
        date_tag = pub_date[0:4] + pub_date[5:7] + pub_date[8:10]
        print "SID=", sid, "Date=", date_tag, pub_date
    
        # get topic id
        c.execute("SELECT tid, id from gl_topic_assignments WHERE id = %s", sid)
        tid, id = c.fetchone()
        
        if tid == "General":
            tid = 8
        elif tid == "Tail":
            tid = 10
        elif tid == "Wing":
            tid = 11
        elif tid == "Fuselage":
            tid = 12
        elif tid == "finishkit":
            tid = 13
        elif tid == "Engine":
            tid = 14
        elif tid == "Cowling":
            tid = 15
        elif tid == "electrical":
            tid = 16
        elif tid == "instpanel":
            tid = 17
        elif tid == "final":
            tid = 18
        elif tid == "Flighttest":
            tid = 19
        elif tid == "Paint":
            tid = 20
        elif tid == "wisdom":
            tid = 21
        elif tid == "accident":
            tid = 22
            
    
        # get story images, if any
        c.execute("SELECT ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid=%s", id)
        img_array = c.fetchmany(20)
        imgs=[]
        img_nums=[]
        img_alts=[]
        if c.rownumber > 0:
            # print "Story Images:"
            for row in img_array:
                ai_img_num, ai_filename = row
                # print ai_img_num, ai_filename
                imgs.append(ai_filename)
                img_nums.append(ai_img_num)
    
        Joomla_intro, Joomla_body = new_p(introtext, bodytext, date_tag, imgs, img_nums)
        
        GLwriter.writerow([title.encode('utf-8'), tid, 'No parent', Joomla_intro.encode('utf-8'), Joomla_body.encode('utf-8'), pub_date, 431, hits, 1, pub_date, pub_date, '0000-00-00 00:00:00', '', 1, 1, '*', sid])
        c.execute("UPDATE gl_stories SET export_flag=1 WHERE sid =%s", sid)
        
        

    csvfile.close()



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
        # print "Story Images:"
        for row in img_array:
            ai_img_num, ai_filename = row
            # print ai_img_num, ai_filename
            imgs.append(ai_filename)
            img_nums.append(ai_img_num)
        

    Joomla_intro, Joomla_body = new_p(introtext, bodytext, sid[:8], imgs, img_nums)
    # print "Returned para"
    print Joomla_intro
    
    print "==============================\n=============================="
    print Joomla_body
    # Typical pattern if image is hardcoded:
    # <img width="300" height="132" align="right" src="http://www.kilohotel.com/rv8/images/articles/20030507210918708_1.jpg" alt="">
    
    # output of BeautifulSoup html5 parser (other parsers fail due to missing </img> tag):
    # <img align="right" alt="" height="132" src="http://www.kilohotel.com/rv8/images/articles/20030507210918708_1.jpg" width="300"/>


def new_p(p, p2, date, imgs, img_nums):
    """move images to required directories, and create new <p> in format required by Joomla with modal extension
    convert the image tags from Geeklog [image1_left] to Joomla + Modal extension tags
    convert hard coded paths from Geeklog image directory to Joomla image directory
    insert the artice publication date into the content paragraph, for extraction 
      after the content is imported into Joomla
    
    Notes:
    1. Articles published prior to 08 Jan 2005 have hard coded images in the html, with no thumbnails.
    2. Articles published from 08 Jan 2005 to 13 Oct 2014 have hard coded images, with thumbnails
    3. Articles published after 13 Oct 2014 have [image1_left] tags, and the images listed in the database
    4. Some articles published on all dates have no images.
    
    return the converted html text block"""

    # sample hard coded image with thumbnail <a href="images/20141013153858942_2_original.jpg" title="View unscaled image"><img width="299" height="199" align="left" src="images/20141013153858942_2.jpg" alt=""></a>
    # joomla equivalent <a href="images/20141013/20141013153858942_2.jpg" class="modal" title="View unscaled image"><img style="margin: 5px; float: left;" src="images/20141013/20141013153858942_2.jpg"  alt=""/>
    
     
    img_codes=[]
    image_dir = base_img_dir + date
    try:
        os.mkdir(image_dir, 0o775)
    except OSError, error:
        print error
        
    for n, img_thumb in enumerate(imgs):
        file_name_parts=img_thumb.split('.')
        img = file_name_parts[0] + '_original.' + file_name_parts[1]
        
        joomla_thumb_full_path = base_img_dir + date + '/' + img_thumb
        joomla_thumb = joomla_img_dir + date + '/' + img_thumb
        
        joomla_img_full_path = base_img_dir + date + '/' + img
        joomla_img = joomla_img_dir + date + '/' + img
        
        try:
            shutil.copy2(gl_img_dir + img_thumb, joomla_thumb_full_path)
        except OSError, error:
            print error
        try:
            shutil.copy2(gl_img_dir + img, joomla_img_full_path)
        except IOError:
            # print "***", img, "thumbnail image not present"
            pass
            
        geeklog_code_left = '[image' + str(img_nums[n]) + '_left]'
        geeklog_code_right = '[image' + str(img_nums[n]) + '_right]'
        geeklog_code_no_align = '[image' + str(img_nums[n]) + ']'
        
        joomla_code_left='<a href="' + joomla_img + '"><img style="margin: 5px; float: left;" src="' + joomla_thumb + '" /></a>'
        joomla_code_right='<a href="' + joomla_img + '"><img style="margin: 5px; float: right;" src="' + joomla_thumb + '" /></a>'
        joomla_code_no_align='<a href="' + joomla_img + '"><img style="margin: 5px;" src="' + joomla_thumb + '" /></a>'
        
        joomla_img_path = joomla_img_dir + date + "/"
        
        p=p.replace(geeklog_code_left, joomla_code_left)
        p=p.replace(geeklog_code_right, joomla_code_right)
        p=p.replace(geeklog_code_no_align, joomla_code_no_align)
        p=p.replace(hard_code_gl_img_dir, joomla_img_path)
        p=p.replace(hard_code_gl_img_dir2, joomla_img_path)

        p2=p2.replace(geeklog_code_left, joomla_code_left)
        p2=p2.replace(geeklog_code_right, joomla_code_right)
        p2=p2.replace(geeklog_code_no_align, joomla_code_no_align)
        p2=p2.replace(hard_code_gl_img_dir, joomla_img_path)
        p2=p2.replace(hard_code_gl_img_dir2, joomla_img_path)
    
    p=p.replace('\n', '').replace('\r', '')    
    p2=p2.replace('\n', '').replace('\r', '') 
       
    soup = BeautifulSoup(p,"html5lib")
    soup2 = BeautifulSoup(p2,"html5lib")
    # global a_tag
    a_tag=soup('a')
    a_tag2=soup2('a')
    img_tag = soup('img')
    img_tag2 = soup2('img')

    for n, item in enumerate(a_tag):
        if thumbnail.match(str(item)):
            # print "thumbnail present"
            a_tag[n]['class']='modal'
        # else:
        #     print "no thumbnail present"
                
    for n, item in enumerate(a_tag2):
        if thumbnail.match(str(item)):
            # print "thumbnail present"
            a_tag2[n]['class']='modal'
            
    for n, item in enumerate(img_tag):
        img_tag[n]['style']='margin: 5px;'
            
    # insert Geeklog article publication date in <p> tag as first element of the intro body tag
    # DT='***DateTime:' + date
    # date_tag=soup.new_tag('p')
    # date_tag.insert(0,DT)
    # soup.body.insert(0,date_tag)
    
    # convert to single string with the contents of the body tag    
    intro = ''
    body = ''
    for tag in soup.body.contents:
        intro += unicode(tag).strip()
    
    for tag in soup2.body.contents:
        body += unicode(tag).strip()
    
    return intro, body
    
    

parse_all()
# parse_one(20141216012305720) # new article, with [image1_left] codes
# parse_one(20030507210918708) # old article with images in Geelog format, and no thumbnails
# parse_one(2002102621491281) # very first article, with hard coded images
# parse_one(20141013153858942) #  sample with hard coded images and thumbnails - need to add class="modal"
# parse_one(20030701205830485) # no images
# parse_one(20030824210346818) # with body text too, but no images
# parse_one(20030105192759933) # body, with image, and phpwebhosting url
