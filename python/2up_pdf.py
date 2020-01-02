#! /opt/local/bin/python2.7

"""
Create a 2-up pdf document from another pdf document

The path to one pdf file must be passed as an argument.
The resulting pdf file has the pages sorted so it can be
cut in half with a slicer, and the pages on the right will
be the second half of the document.  I.e., if the original
pdf file has 5 pages, the resulting 2-up document with 
have the following page layout

2-up page 1: original page 1, original page 4
2-up page 2: original page 2, original page 5
2-up page 3, original page 3
"""

import sys
from PyPDF2 import PdfFileReader
import os

temp_dir = '/Users/kwh/temp'
temp_name = 'latex_temp.tex'
temp_path = os.path.join(temp_dir, temp_name)

def make_page_list(num_pages):
    if not num_pages % 2:
        # even number of pages
        mid = num_pages / 2 + 1
    else:
        # odd number of pages
        mid = num_pages / 2 + 2

    first_half_iter = iter(range(1, mid))
    second_half_iter = iter(range(mid, num_pages+1))
    page_list = []
    
    # debug two sets of pages
    # print range(1, mid)
    # print range(mid, num_pages+1)

    while 1:
        try:
            page_list.append(first_half_iter.next())
            page_list.append(second_half_iter.next())
        except StopIteration:
            try:
                page_list.append(first_half_iter.next())
            except StopIteration:
                try:
                    page_list.append(second_half_iter.next())
                except StopIteration:
                    print page_list
                    # sys.exit()
                    return repr(page_list)[1:-1]

def make_latex(file_path, sorted=False):
    num_pages = PdfFileReader(file(file_path)).getNumPages()
    LATEX = file(temp_path, 'w')
    if sorted:
        # put the pages in normal order, i.e. the first page in the 2-up file will hold pages 1 and 2 of the original file.
        latex = "\documentclass[a4paper, landscape]{article} \usepackage{pdfpages} \\begin{document} \includepdf[nup=2x1,pages=-]{%s} \end{document}" % file_path
    else:
        # put the pages so the first half of the pages from the original file are on the left
        latex = "\documentclass[a4paper, landscape]{article} \usepackage{pdfpages} \\begin{document} \includepdf[nup=2x1,pages={%s}]{%s} \end{document}" % (make_page_list(num_pages), file_path)
    LATEX.write(latex)
    
    # need to force the file to be written before we try to use it.
    LATEX.close()
    
    # run latex
    result = os.spawnlp('P_WAIT','pdflatex', 'pdflatex', temp_path, 'temp.pdf')
    # remove the .aux and .log files from this latex run
    # os.spawnlp('P_WAIT', 'rm', 'rm', '-f', 'latex_temp.aux', 'latex_temp.log')
    temp_pdf_name = os.path.splitext(temp_name)[0] + '.pdf'
    pdf_name = os.path.splitext(file_path)[0] + '_2up.pdf'
    os.execlp('mv', 'mv', temp_pdf_name, pdf_name)

if __name__ == '__main__':
    usage = """
Usage: 2up_pdf.py [-c] path_to_pdf_file

A '-c' (optional), produces a pdf that has the pages sorted so that it can 
be cut in half, and the left side pages will be the first half, with the 
right side pages in the second half.
    """
    if len(sys.argv) == 2:
        # if sys.argv[1] == '-h':
        #     print usage
        #     exit()
        try:
            make_latex(sys.argv[1], sorted=True)
        except IOError:
            print usage
    elif len(sys.argv) == 3:
        if sys.argv[1] != '-c':
            print usage
        else:
            make_latex(sys.argv[2], sorted=False)
    else:
        print usage
