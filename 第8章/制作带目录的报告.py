# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""

import numpy as np
import pandas as pd
from reportlab.platypus import BaseDocTemplate,PageTemplate,NextPageTemplate,Paragraph
from reportlab.platypus import Frame, Table, TableStyle,Spacer,PageBreak,FrameBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors 
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
class MyDocTemplate(BaseDocTemplate):
    def __init__(self,filename):
        super().__init__(filename)
        f0=Frame(0, 400, 1200, 50,id='f0',showBoundary=0)
        f1=Frame(900, 120, 250, 30,id='f1',showBoundary=0)
        tpl_covers = PageTemplate('tpl_covers',[f0,f1],header_covers,pagesize=(1200,800))
        f2=Frame(50, 50, 700, 900,id='f2',showBoundary=0)
        tpl_catalog = PageTemplate('tpl_catalog',[f2],pagesize=(800,1000))
        f3=Frame(0, 750, 1000, 50,id='f3',showBoundary=0)
        f4=Frame(0, 400, 1200, 300,id='f4',showBoundary=0)
        f5=Frame(0, 50, 600, 350,id='f5',showBoundary=0)
        f6=Frame(600, 50, 600, 350,id='f6',showBoundary=0)
        tpl_body  = PageTemplate('tpl_body',[f3,f4,f5,f6],header_body,pagesize=(1200,800))
        self.addPageTemplates([tpl_covers,tpl_catalog,tpl_body])
    def afterFlowable(self, flowable):
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'A1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'A2':
                self.notify('TOCEntry', (1, text, self.page))
def header_covers(c, doc):  
    c.saveState()
    c.drawImage(r'H:\示例\第8章\background.png',0,500,1200,300)
    c.drawImage(r'H:\示例\第8章\logo.png',0,800-72,190,72)
    c.setFont('微软雅黑',30)
    c.drawCentredString(600, 300, '南山研究院 分析师 金融哥')
    c.setFont('微软雅黑',20)
    c.drawString(50, 120, '因 / 为 / 专 / 注 / 所 / 以 / 专 / 业')
    c.setLineWidth(10)
    c.line(0, 100,1200 ,100 )
    c.setFont('微软雅黑',15)
    c.drawString(50, 80, '本产品保密并受到版权法保护')
    c.drawRightString(1150, 80, 'Confidential and Protected by Copyright Laws')
    c.setFillColor(colors.red)
    c.rect(800, 500, 1200, 20, stroke=0, fill=1)
    c.setFillGray(0.75)
    c.rect(0, 500, 800, 20, stroke=0, fill=1)
    c.restoreState()              
def header_body(c, doc):  
    c.saveState()
    pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
    c.drawImage(r'H:\示例\第8章\logo.png',1200-190,800-72,190,72)
    c.setLineWidth(3)
    c.line(0, 50,1200 ,50 )
    c.line(0, 800-75,1200 ,800-75 )
    c.setFont('微软雅黑',20)
    c.drawString(50, 30, '本产品保密并受到版权法保护')
    c.drawRightString(1150, 30, 'Confidential and Protected by Copyright Laws')
    page_num = c.getPageNumber()
    c.setFont('微软雅黑',30)
    text = '第 %s 页' % page_num
    c.drawRightString(580,20, text)
    c.restoreState()
def table(data): 
    table=Table(data)
    table.setStyle(TableStyle([
            ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
            ('BOX',(0,0),(-1,-1),0.25,colors.black),
            ('FONT',(0,0),(-1,-1),'微软雅黑',20),]))
    return table
def bar(data):  
    drawing=Drawing(500,250)
    bar=VerticalBarChart()
    bar.x,bar.y,bar.height,bar.width=20,-20,270,560
    bar.data,bar.strokeColor=[data[1]],colors.black
    bar.valueAxis.valueMin,bar.barLabels.nudge=0,18
    bar.barLabelFormat,bar.valueAxis.valueMax='%0.1f',100
    bar.valueAxis.labels.fontSize = 20
    bar.categoryAxis.labels.fontName='微软雅黑'
    bar.categoryAxis.labels.fontSize,bar.barLabels.fontSize = 20,30
    bar.categoryAxis.labels.dx,bar.categoryAxis.labels.dy=0,0
    bar.categoryAxis.categoryNames = data[0]
    bar.bars[0].fillColor = colors.black
    drawing.add(bar)
    return drawing

styles=getSampleStyleSheet()
Para_S = ParagraphStyle
styles.add(Para_S(name='A1',fontName='微软雅黑',fontSize=40))
styles.add(Para_S(name='A2',fontName='微软雅黑',fontSize=25,leading=25))
styles.add(Para_S(name='A3',fontName='微软雅黑',fontSize=20,leading=30,spaceBefore=10)) 
styles.add(Para_S(name='A4',fontName='微软雅黑',fontSize=25,alignment=1,spaceAfter=30))    
styles.add(Para_S(name='A5',fontName='微软雅黑',fontSize=50,alignment=1,spaceAfter=30))    
styles.add(Para_S(name='A6',fontName='微软雅黑',fontSize=30,alignment=1,spaceAfter=30))   
styles['A3'].firstLineIndent=40
story=[]
story.append(Paragraph('上市公司财务分析报告',styles['A5'])) 
story.append(Paragraph('2020年4月',styles['A6'])) 
story.append(NextPageTemplate('tpl_catalog'))
story.append(PageBreak())
story.append(Paragraph('目    录',styles['A6']))  
story.append(Spacer(1, 20))
toc = TableOfContents()
toc.levelStyles = [styles['A2'], styles['A3']]
story.append(toc)
story.append(NextPageTemplate('tpl_body'))
story.append(PageBreak())
list=['上海公司','四川公司','重庆公司','深圳公司']
for i in list:
    df = pd.read_excel(r'H:\示例\第8章\公司数据.xlsx', sheet_name =i,header=None)
    df1=df.iloc[:9,:]
    dataA_0=np.array(df1).tolist()
    df2=df.iloc[[0,9],1:]
    dataB_0=np.array(df2).tolist()
    name=df.iloc[10,1]
    textA_0,textB_0=df.iloc[11,1],df.iloc[12,1]
    title0=name+'财务分析报告'
    story.append(Paragraph(title0,styles['A1'])) 
    story.append(FrameBreak())
    story.append(Paragraph('公司简介',styles['A2'])) 
    story.append(Paragraph(textA_0,styles['A3'])) 
    story.append(Spacer(1, 12))
    story.append(Paragraph('经营范围',styles['A2'])) 
    story.append(Paragraph(textB_0,styles['A3']))   
    story.append(FrameBreak())
    story.append(Paragraph('主要财务比率一览表',styles['A4'])) 
    story.append(table(dataA_0))
    story.append(FrameBreak())
    story.append(Paragraph('近五年存货周转天数图示(单位：天)',styles['A4'])) 
    story.append(bar(dataB_0))
    story.append(FrameBreak())
doc = MyDocTemplate(r'H:\示例\第8章\MyDocTemplate.pdf')
doc.multiBuild(story)

