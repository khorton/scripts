#! /opt/local/bin/python3.7

patterns = ['April 23, 2020 7:30']
app = '/Users/kwh/sw_projects/git/scripts/Automater/Chase_PPP_Page_Update.app'
email_sent_flag = "/Users/kwh/temp/Chase_Page_Update_Email_Sent"

# noapp = '/Users/kwh/temp/Chase_PPP_Page_NoUpdate.app'

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

import subprocess

import re
from pathlib import Path

# set the url as VentureBeat,
url = "https://www.chase.com/cares"

# set the headers like we are a browser,
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# download the homepage
response = requests.get(url, headers=headers)

# parse the downloaded homepage and grab all text, then,
soup = BeautifulSoup(response.text, "lxml")
updated_time=soup.find_all(string=re.compile("Updated"))
result = str(updated_time)

for pattern in patterns:
	print('Looking for "%s" in "%s" ->' % (pattern, result), end=' ')

	if re.search(pattern,  result):
		print('No page update')
	else:
		print('Page updated!!')
		my_file = Path(email_sent_flag)
		if my_file.is_file():
			print('Page updated, but flag present!!')
		else:
			Path(email_sent_flag).touch()
			subprocess.call(
				["/usr/bin/open", "-W", "-n", "-a", app]
				)


