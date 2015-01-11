#! /usr/bin/env python

#mysql python docs at https://github.com/farcepest/MySQLdb1/blob/master/doc/user_guide.rst#mysqldb

import MySQLdb
import sys
import csv
import re

db=MySQLdb.connect(user='root',passwd="Yarmouth2",db="rv8_merge")
c=db.cursor()

# sid=2015010420254995
# c.execute("SELECT ai_sid, ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid = %s", sid)
# array = c.fetchmany(10)
# for row in array:
#     (sid, num, iid) = row
#     print sid, num, iid

# sid = 2015010420254995
sid = 20141220235836599 # no images
c.execute("SELECT ai_img_num, ai_filename FROM gl_article_images WHERE ai_sid=%s", sid)
img_array = c.fetchmany(20)
if c.rownumber > 0:
    for row in img_array:
        ai_img_num, ai_filename = row
        print ai_img_num, ai_filename
else:
    print "no images"


# c.execute("SELECT sid, uid, date, title, introtext, bodytext, hits, comments FROM gl_stories")
# story_array = c.fetchmany(2000)
# n = 1
# for row in story_array:
#     sid, uid, date, title, introtext, bodytext, hits, comments = row
#     c.execute("SELECT tid, id from gl_topic_assignments WHERE id = %s", sid)
#     tid, id = c.fetchone()
#     print sid
#     print id
#     print tid
#     print uid
#     print date
#     print title
#     print introtext
#     print "Body Text =", bodytext
#     print "Hits =", hits
#
#     n -= 1
#     if n < 1:
#         sys.exit()
