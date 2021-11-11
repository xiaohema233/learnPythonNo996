# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:17:30 2020

@author: Administrator
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import pink, black, red, blue, green
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
c=canvas.Canvas(r"H:\示例\第8章\report.pdf")
c.setPageSize((1200,800))
c.drawImage(r"H:\示例\第8章\background.png",0,500,1200,300)
c.drawImage(r"H:\示例\第8章\logo.png",0,800-72,190,72)
c.setFont('微软雅黑',50)
c.drawCentredString(600, 400,"2020年汽车金融专题研究报告")
c.setFont('微软雅黑',30)
c.drawCentredString(600, 300, "南山研究院 分析师 金融哥")
c.setFont('微软雅黑',20)
c.drawString(50, 120, "因 / 为 / 专 / 注 / 所 / 以 / 专 / 业")
c.setFont('微软雅黑',30)
c.drawRightString(1150, 120, "2020年3月")
c.setLineWidth(10)
c.line(0, 100,1200 ,100 )
c.setFont('微软雅黑',15)
c.drawString(50, 80, "本产品保密并受到版权法保护")
c.drawRightString(1150, 80, "Confidential and Protected by Copyright Laws")
c.setFillColor(red)
c.rect(800, 500, 1200, 20, stroke=0, fill=1)
c.setFillGray(0.75)
c.setFillAlpha(0.3)
c.rect(0, 500, 800, 20, stroke=0, fill=1)
c.showPage()
c.save()
