# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:39:22 2020

@author: Administrator
"""

import xlsxwriter
wb = xlsxwriter.Workbook(r"H:\示例\第5章\生成Excel图表.xlsx")
ws = wb.add_worksheet()
ws.write(0,0,'部门')
ws.write("A1",'部门')
f_title = wb.add_format({'border':1,'align':'center','font_size':12,'bold':True})
f_num = wb.add_format()
f_num.set_border(1)
f_num.set_align('center')
f_num.set_num_format('0.00')
ws.write("A1",'部门',f_title)
title = ['部门','态度考核','成效考核','工作能力','出勤率','综合得分']
ws.write_row('A1', title,f_title)
ws.write_column('A2', ['部门1','部门2','部门3'],f_title)
ws.write_row('B2', [19.20,28.00,26.30,17.30],f_num)
ws.write_row('B3', [18.85,24.00,25.35,19.10],f_num)
ws.write_row('B4', [19.10,27.00,25.71,17.52],f_num)
ws.write_formula('F2','=(0.2*B2+0.3*C2+0.3*D2+0.2*E2)',f_num)
ws.write_formula('F3','=(0.2*B3+0.3*C3+0.3*D3+0.2*E3)',f_num)
ws.write_formula('F4','=(0.2*B4+0.3*C4+0.3*D4+0.2*E4)',f_num)
ws.merge_range('G6:I10',"")
ws.write_rich_string('G6','成效考核',f_title,'部门1','得分：28.00')
ws.write_comment('F15',"作者：HHP")
ws.show_comments()
ws.set_column(0, 5, 11)
ws.insert_image('G1',r'H:\示例\第5章\pic.png',{'x_scale':0.2,'y_scale':0.2})
chart =wb.add_chart({'type': 'column'})
for r in range(2,5):
    r=str(r)
    chart.add_series({
    'categories': '=Sheet1!$B$1:$E$1',
    'values': '=Sheet1!$B$'+r+':$E$'+r,
    'line': {'color': 'black'},'name': '=Sheet1!$A$'+r,
    'data_labels': {'value': True,'num_format': '0'}
    })
chart.set_title({'name':'各部门考核情况'})
ws.insert_chart('A6',chart)
wb.close()



