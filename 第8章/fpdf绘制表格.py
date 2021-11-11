# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""

from fpdf import FPDF
pdf=FPDF(format='letter', orientation='L',unit='cm')
pdf.add_page()
pdf.add_font('msyh','','H:\示例\第8章\msyh.ttf', uni=True)
pdf.set_font('msyh','',20)
effective_page_width = pdf.w - 2*pdf.l_margin
pdf.cell(effective_page_width,1,txt='产品销售情况表', align="C",border=0)
pdf.ln(1.5)
pdf.cell(10,1,txt='', align="C",border=0)
pdf.cell(2,1,txt='产品', align="C",border=1)
pdf.cell(2,1,txt='销量', align="C",border=1)
pdf.cell(2,1,txt='金额', align="C",border=1)
pdf.ln(1)
pdf.cell(10,1,txt='', align="C",border=0)
pdf.cell(2,1,txt='电脑', align="C",border=1)
pdf.cell(2,1,txt='100', align="C",border=1)
pdf.cell(2,1,txt='500', align="C",border=1)
pdf.ln(1)
pdf.cell(10,1,txt='', align="C",border=0)
pdf.cell(2,1,txt='手机', align="C",border=1)
pdf.cell(2,1,txt='200', align="C",border=1)
pdf.cell(2,1,txt='800', align="C",border=1)
pdf.output(r'H:\示例\第8章\test_table.pdf')


