txt_0='什么是汽车金融？'
txt_1='''汽车金融是汽车全产业链覆盖的资本流动。狭义的汽车金融隶属于消费金融,广义的汽车金融贯穿全产业链。汽车金融的概念最早源于美国，狭义的汽车金融，更多地关注汽车销售环节，为下游客户提供融资性金融服务,隶属于消费金融。广义的汽车金融，是贯穿汽车的生产、流通、销售、使用回收等环节中的资金流动，提高资本利用率和资金周转率。'''
txt_2='''我国汽车消费金融业萌芽于商业银行贷款，后经政策放宽，形成汽车金融公司、汽车融资租赁公司、互联网汽车金融公司等多元主体并存的局面。'''
txt_3='''中国汽车消费金融渗透率与海外成熟市场差距很大。汽车金融的渗透率，指通过贷款、融资等金融方式购买的车辆数量与汽车销量之比。中国汽车消费金融渗透率一直处于较低水平。'''

from reportlab.lib.styles import getSampleStyleSheet
s = getSampleStyleSheet()
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
s["Title"].fontName,s["Title"].fontSize='微软雅黑' ,30
s["Title"].spaceAfter,s["Normal"].spaceBefore=30,10
s["Normal"].fontName,s["Normal"].fontSize='微软雅黑',20
s["Normal"].leading= 30
s["Normal"].firstLineIndent = 40
from reportlab.platypus import Paragraph
p_0=Paragraph(txt_0,s["Title"])
p_1=Paragraph(txt_1,s["Normal"])
p_2=Paragraph(txt_2,s["Normal"])
p_3=Paragraph(txt_3,s["Normal"])
story_text = [p_0,p_1,p_2,p_3]

data = [["姓名","一季度","二季度","三季度","四季度"],
["小赵",100,110,125,135], ["小钱",110,114,126,123],
["小孙",120,115,127,141],["小李",130,117,128,165],
["小王",120,127,122,125]]
col_widths, row_heights =[80,100,100,100,100],[60,50,50,50,50,50]
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
table_style  = TableStyle([
        ('FONT', (0, 0), (0, -1), '微软雅黑', 30),
        ('FONT', (0, 0), (-1, 0), '微软雅黑', 30),
        ('FONT', (1, 1), (-1, -1), '微软雅黑', 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('BACKGROUND',(0,0),(-1,-1),colors.white)])
from reportlab.platypus import Table
table=Table(data,colWidths=col_widths,rowHeights=row_heights,style=table_style)
tabletitle='''<para alignment=center fontName='微软雅黑' fontSize=20 spaceAfter=30>表1： 销售情况表</para>'''
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
story_table = [Paragraph(tabletitle,styles['Normal']),table]

from reportlab.graphics.shapes import Drawing
d = Drawing(100, 100)
from reportlab.graphics.charts.barcharts import VerticalBarChart
bar = VerticalBarChart()
bar.x,bar.y,bar.height,bar.width,bar.valueAxis.valueMin=50,-150,280,500,0
bar.categoryAxis.categoryNames=['2012','2013','2014','2015','2016']
bar.data = [[16, 17, 18, 24, 25]]
bar.bars[0].fillColor,bar.barLabels.nudge=colors.black,18
bar.barLabelFormat,bar.valueAxis.labels.fontSize='%0.0f',20
bar.categoryAxis.labels.fontSize,bar.barLabels.fontSize=20,30
d.add(bar)
from reportlab.platypus import Spacer
story_chart=[Spacer(1,75),d]

from reportlab.platypus import Frame
f1 = Frame(0, 0, 600, 400, showBoundary=1, id='f1')
f2 = Frame(600, 0, 600, 400, showBoundary=1, id='f2')
f3 = Frame(0, 400, 1200, 400, showBoundary=1, id='f3')
from reportlab.pdfgen.canvas import Canvas
c = Canvas(r'H:\示例\第8章\mydoc_Frame.pdf')
c.setPageSize((1200,800))
f1.addFromList(story_chart,c)
f2.addFromList(story_table,c)
f3.addFromList(story_text,c)
c.save()
