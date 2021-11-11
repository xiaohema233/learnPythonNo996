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
from reportlab.platypus import Paragraph
story_table = [Paragraph(tabletitle,styles['Normal']),table]
from reportlab.platypus import SimpleDocTemplate
doc = SimpleDocTemplate(r'H:\示例\第8章\mydoc_table.pdf',pagesize=(1200,800))
doc.build(story_table)