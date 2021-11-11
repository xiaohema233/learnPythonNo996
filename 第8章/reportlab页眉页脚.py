# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:17:30 2020

@author: Administrator
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph,PageBreak, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
def header_footer(c, doc):
    c.drawImage(r"H:\示例\第8章\logo.png",1200-190,800-72,190,72)
    c.setFont('微软雅黑',20)
    c.drawString(50, 60, "因 / 为 / 专 / 注 / 所 / 以 / 专 / 业")
    c.setLineWidth(3)
    c.line(0, 50,1200 ,50 )
    c.line(0, 800-75,1200 ,800-75 )
    c.setFont('微软雅黑',20)
    c.drawString(50, 30, "本产品保密并受到版权法保护")
    c.drawRightString(1150, 30, "Confidential and Protected by Copyright Laws")
    page_num = c.getPageNumber()
    c.setFont('微软雅黑',30)
    text = "第 %s 页" % page_num
    c.drawRightString(580,20, text)
    c.setFont('微软雅黑',50)
    c.rotate(30)
    c.setFillAlpha(0.2)
    c.drawString(600, 0, '版权所有 南山金融研究')
    c.rotate(-30)
myPDF = SimpleDocTemplate(r'H:\示例\第8章\mydoc.pdf',pagesize=(1200,800))
story = []
list=["2020年汽车金融专题研究报告","2020年消费金融专题研究报告",         
"2020年融资租赁专题研究报告","2020年汽车销售专题研究报告"]
styles = getSampleStyleSheet()
styles["Normal"].fontName='微软雅黑' 
styles["Normal"].fontSize=40
for item in list:
    story.append(Spacer(1,200))
    story.append(Paragraph(item, styles["Normal"]))
    story.append(PageBreak())
myPDF.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
