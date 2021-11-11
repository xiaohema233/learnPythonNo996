# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
file= r"H:\示例\第8章\MyDocTemplate.pdf"
rsrcmgr = PDFResourceManager()
outfp = io.StringIO()
device= TextConverter(rsrcmgr, outfp)
interpreter = PDFPageInterpreter(rsrcmgr, device)
with open(file, 'rb') as fp:
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    text = outfp.getvalue()
print(text)
device.close()
outfp.close()

