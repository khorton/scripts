#! /usr/bin/env python

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

import re
# set the url as VentureBeat,
url = "https://www.chase.com/cares"
# set the headers like we are a browser,
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# download the homepage
response = requests.get(url, headers=headers)
# parse the downloaded homepage and grab all text, then,
soup = BeautifulSoup(response.text, "lxml")
updated_time=soup.find_all(string=re.compile("Updated"))
print updated_time