#! /usr/bin/env python

#mysql python docs at https://github.com/farcepest/MySQLdb1/blob/master/doc/user_guide.rst#mysqldb

import MySQLdb
import sys
import csv
from bs4 import BeautifulSoup

db=MySQLdb.connect(user='root',passwd="Yarmouth2",db="rv8_merge")
c=db.cursor()

# sid=2015010420254995
# c.execute("SELECT ai_sid, ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid = %s", sid)
# array = c.fetchmany(10)
# for row in array:
#     (sid, num, iid) = row
#     print sid, num, iid

# sid = 2015010420254995 # with images
# sid = 20141220235836599 # no images
# c.execute("SELECT ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid=%s", sid)
# img_array = c.fetchmany(20)
# if c.rownumber > 0:
#     for row in img_array:
#         ai_img_num, ai_filename = row
#         print ai_img_num, ai_filename
# else:
#     print "no images"


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

# parse_all()
parse_one(2015010420254995)