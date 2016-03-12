#!/sw/bin/python

import glob
import re
import sys
import shutil
import subprocess
import os

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
    

def extract_PDF_data(fname):
    text = pdftext = convert(fname)
    try:
        # Is this an instrument approach chart?
        AD_Name_re = re.compile('(\w{4})-IAP')
        AD_results = AD_Name_re.search(text)
        airport_ID = AD_results.group(1)
        # print airport_ID,  "Approach Chart"
        
        IAP_Name_re = re.compile('(.+RWY.+)')
        IAP_results = IAP_Name_re.search(text)
        IAP_ID = IAP_results.group()
        
        # replace slashes with dashes, as slashes are file pathc separators in Unix
        rep_re = re.compile('/')
        IAP_ID = rep_re.sub('-', IAP_ID)
        # print IAP_ID
        # type = "AP"
        return airport_ID, IAP_ID + ".pdf"
    except AttributeError:
        # print("Not an IAP chart")
        # print(text)
        pass

    try:
        # Is this an aerodrome chart?
        AD_Name_re = re.compile('(\w{4})-AD')
        AD_results = AD_Name_re.search(text)
        airport_ID = AD_results.group(1)
        # print "Aerodrome Chart for", airport_ID
        return airport_ID, "Aerodrome Chart.pdf"
    except AttributeError:
        print("Not an airport chart")
        
        
        

# extract_airport_IAP("/Users/kwh/ownCloud/temp/GRT_CAP_PDFs/e-CAP4_4February2016(1) - Page 19.pdf")


if __name__ == '__main__': 
    dir = '/Users/kwh/ownCloud/temp'
    
    in_file = '/Users/kwh/ownCloud/temp/GRT_CAP_PDFs/test/1e-CAP4_4February2016(1) - Page 15-40.pdf'
    
    return_code = subprocess.call(['pdftk', in_file, 'burst'])
    print return_code
    # sys.exit()
    
    pdfs = glob.glob(dir + '/*.pdf')
    for pdf in pdfs:
        ID, file_name = extract_PDF_data(pdf)
        print ID, file_name
        try:
            shutil.move(pdf, dir + "/Plates/" + ID + "/" + file_name)
        except IOError:
            os.makedirs(dir + "/Plates/" + ID)
            shutil.move(pdf, dir + "/Plates/" + ID + "/" + file_name)
            
        

    # sys.exit()

""" pdftk test.pdf update_info metadata.txt output test3.pdf allow printing owner_pw password
metadata.txt has the following (without the comment characters)
InfoKey: Subject
InfoValue: Licensed to Peter Burrowes
"""