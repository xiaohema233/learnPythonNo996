# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:57:00 2020

@author: Administrator
"""

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
file=r'G:\示例\第8章\扫描版PDF_OCR.pdf'
f=open(file, 'rb')
pages=PDFPage.get_pages(f,caching=True,check_extractable=True)
text=""
for page in pages:
	rm = PDFResourceManager()
	data = io.StringIO()
	converter= TextConverter(rm, data)
	page_interpreter = PDFPageInterpreter(rm, converter)
	page_interpreter.process_page(page)
	text = text+data.getvalue()
print(text)