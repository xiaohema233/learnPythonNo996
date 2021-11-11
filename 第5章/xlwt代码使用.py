# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:39:22 2020

@author: Administrator
"""

import xlwt
wb=xlwt.Workbook()
ws=wb.add_sheet('abc')
ws.write(0,0,1000)
style0=xlwt.Style.XFStyle()
style0=xlwt.XFStyle()
style0.alignment.horz=xlwt.Alignment.HORZ_CENTER
style0.alignment.vert=xlwt.Alignment.VERT_CENTER
style0.borders.bottom=xlwt.Borders.THICK
style0.borders.bottom_colour=xlwt.Style.colour_map['green']
style0.font.name= 'Arial'
style0.font.colour_index= xlwt.Style.colour_map['red']
style0.font.bold=True
ws.write(1,0,1000,style0)

pt=xlwt.Pattern()
pt.pattern=xlwt.Pattern.SOLID_PATTERN
pt.pattern_fore_colour=xlwt.Style.colour_map['red']
pt.pattern,pt.pattern_fore_colour


style1=xlwt.XFStyle()
style1.pattern=pt
ws.write(2,0,1000,style1)
style2=xlwt.XFStyle()
style2.num_format_str='$#,##0.00'
ws.write(3,0,1000,style2)

import datetime
style3=xlwt.XFStyle()
style3.num_format_str='m/d/yy h:mm'
ws.write(0, 1, datetime.datetime.now(), style3)
from xlwt import easyxf
style4=easyxf(
'align:vertical center, horizontal center;'
'font:name 微软雅黑,bold True,colour white;'
'borders: bottom_colour blue, bottom thick;'
'pattern: pattern solid, fore_colour blue;',
num_format_str='m/d/yy h:mm')
ws.write(1,1,datetime.datetime.now(),style4)

from xlwt import Formula
ws.write(4,0,Formula("$A$1+$A$2*SUM($A$2:$A$4)"))

ws.write_merge(0,4,2,3,"这是一个合并单元格",style0)

ws.row(5).write(0,'这是表格A5')
ws.row(5).set_cell_text(1,'这是表格B5')

ws.row(6).set_style(style0)
ws.row(6).height=300
ws.col(0).width=4000
ws.col(1).width=4000
wb.save(r'H:\示例\第5章\xlwt新建表.xls')



