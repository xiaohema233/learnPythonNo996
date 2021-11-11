# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""

from fpdf import FPDF
pdf=FPDF(format='letter', orientation='L',unit='cm')
pdf.add_page()
pdf.add_font('msyh','','H:\示例\第8章\msyh.ttf', uni=True)
pdf.set_font('msyh','',50)
pdf.cell(10,2,txt='PDF文件是什么？')
pdf.ln(3)
text='''
PDF是由Adobe用于与应用程序、操作系统、硬件无关的方式进行文件交换所发展出的文件格式。PDF文件以PostScript语言图象模型为基础，无论在哪种打印机上都可保证精确的颜色和准确的打印效果，即PDF会忠实地再现原稿的每一个字符、颜色以及图象。
'''
pdf.set_font('msyh','',20)
effective_page_width = pdf.w - 2*pdf.l_margin
pdf.multi_cell(effective_page_width,2,txt=text)
pdf.output(r'H:\示例\第8章\test_text.pdf')

