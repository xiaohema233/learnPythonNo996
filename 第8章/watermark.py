# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:09:41 2020

@author: Administrator
"""

from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
pdf = PdfReader("MyDocTemplate.pdf")
canvas = Canvas("MyDocTemplate_out.pdf")
list = [pagexobj(i) for i in pdf.pages]
for obj in list:
	canvas.setPageSize((obj.BBox[2], obj.BBox[3]))
	canvas.doForm(makerl(canvas, obj))
	canvas.saveState()
	canvas.setFont('微软雅黑',50)
	canvas.rotate(30)
	canvas.setFillAlpha(0.2)
	canvas.drawString(400, 0, '版权所有 南山金融研究')
	canvas.rotate(-30)
	canvas.restoreState()
	canvas.showPage()
canvas.save()