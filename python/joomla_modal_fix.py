#! /sw/bin/python

import MySQLdb
import re

db=MySQLdb.connect(user='root',passwd="Yarmouth2",db="joomla3")
c=db.cursor()

match = '%mygroup%'
# c.execute("SELECT alias, created, introtext, fulltext from shj_content WHERE introtext like '%mygroup%' OR fulltext LIKE '%mygroup%' LIMIT 50")
c.execute("SELECT alias, created, introtext, shj_content.fulltext from shj_content where flag2=1")
result_array = c.fetchmany(500)

for result in result_array:
    dt=result[1].strftime('%Y%m%d%H%M%S')
    it=result[2]
    ft=result[3]
