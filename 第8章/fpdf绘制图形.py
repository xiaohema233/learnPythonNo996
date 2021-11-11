# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""

from fpdf import FPDF
pdf=FPDF(format='letter', orientation='L',unit='cm')
pdf.add_page()
pdf.set_line_width(0.1)
pdf.set_fill_color(0, 255, 0)
pdf.line(1, 1, 7, 1)
pdf.rect(2, 2, 3, 3)
pdf.image("H:\示例\第8章\pic.png", x=8, y=2, w=4)
pdf.output(r'H:\示例\第8章\test_shapes.pdf')



