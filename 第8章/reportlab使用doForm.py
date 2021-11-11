# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:17:30 2020

@author: Administrator
"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
c = canvas.Canvas(r'H:\示例\第8章\mydoc_form.pdf')
c.setPageSize((1200,800))
c.beginForm("LOGO")
c.drawImage(r"H:\示例\第8章\logo.png",0,800-72,190,72)
c.endForm()
list=["2020年汽车金融专题研究报告","2020年消费金融专题研究报告",         
"2020年融资租赁专题研究报告","2020年汽车销售专题研究报告"]
for item in list:
	c.doForm("LOGO")
	c.setFont('微软雅黑',80)
	c.drawCentredString(600, 400,item)
	c.showPage()
c.save()
