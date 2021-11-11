# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:02:51 2020

@author: Administrator
"""

import xlsxwriter
wb = xlsxwriter.Workbook('创建带格式图表.xlsx') 
ws = wb.add_worksheet() 
title = ['部门','态度考核','成效考核','工作能力','出勤率','综合得分']
department = ['部门1','部门2','部门3']
data = [[19.20,28.00,26.30,17.30], [18.85,24.00,25.35,19.10], [19.10,27.00,25.71,17.52]]
format_title = wb.add_format() 
format_title.set_border(1) 
format_title.set_align('center')
format_title.set_font_size(12) 
format_title.set_bold()
format_num = wb.add_format()
format_num.set_border(1)
format_num.set_align('center')
format_num.set_num_format('0.00') 
ws.write_row('A1',title,format_title)
ws.write_column('A2',department,format_title)
ws.write_row('B2',data[0],format_num)
ws.write_row('B3',data[1],format_num)
ws.write_row('B4',data[2],format_num)
ws.set_column(0, 5, 11)
chart =wb.add_chart({'type': 'column'})
for r in range(2,5): 
    r=str(r)
    ws.write_formula('F'+ r,'=(0.2*B'+r+'+0.3*C'+r+'+0.3*D'+r+'+0.2*E'+r+')',format_num)
    chart.add_series({'categories': '=Sheet1!$B$1:$E$1', 'values': '=Sheet1!$B$'+r+':$E$'+r,
        'line': {'color': 'black'},'name': '=Sheet1!$A$'+r,
        'data_labels': {'value': True,'num_format': '0'}})
chart.set_title({'name':'各部门考核情况'})
ws.insert_chart('A6',chart)
ws.insert_image('G1', 'pic.png',{'x_scale': 0.2, 'y_scale': 0.2})
wb.close()
