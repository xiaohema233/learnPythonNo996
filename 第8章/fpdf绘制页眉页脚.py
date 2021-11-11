# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""

from fpdf import FPDF
class Template(FPDF):
    def header(self):
        self.image('H:\示例\第8章\logo.png',x=1, y=0, w=5)
        self.ln(1)
    def footer(self):
        self.set_y(-1)
        page = '第 ' +str(self.page_no())+ '页'
        self.cell(pdf.w - 2*pdf.l_margin, 1, page, align='C')
pdf=Template(format='letter',unit='cm')
pdf.add_font('msyh','','H:\示例\第8章\msyh.ttf', uni=True)
pdf.add_page()
with open(r'H:\示例\第8章\case.txt','r') as f:
    text=f.read()
pdf.set_font('msyh','',30)
effective_page_width = pdf.w - 2*pdf.l_margin
pdf.multi_cell(effective_page_width,2,txt=text)
pdf.output(r'H:\示例\第8章\header_footer.pdf')