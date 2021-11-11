# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
from win32com.client import constants,DispatchEx
import pandas as pd
df = pd.DataFrame(pd.read_excel(r'H:\示例\第6章\书签应用\成绩汇总表.xlsx'))
df= df[['姓名', '课程编号', '课程名称', '成绩']]
names=df['姓名'].drop_duplicates().values.tolist()	
wordApp = DispatchEx('Word.Application')
for name in names:
    myDoc=wordApp.Documents.Open(r'H:\示例\第6章\书签应用\成绩单模板.docx')
    df1=df[df['姓名']==name]
    rows=len(df1)
    df2= df1[['课程编号','课程名称','成绩']]
    bm=myDoc.Bookmarks("姓名")
    bm.Range.Text = name
    bmRange=myDoc.Bookmarks("成绩表").Range
    table = myDoc.Tables.Add(bmRange, rows+1, 3)
    table.Borders.Enable = 1
    table.Cell(1, 1).Range.Text = '课程编号'
    table.Cell(1, 2).Range.Text = '课程名称'
    table.Cell(1, 3).Range.Text = '成绩'
    for i in range(rows):
        for j in range(3):
            table.Cell(i+2, j+1).Range.Text = str(df2.iloc[i,j])
    myDoc.SaveAs(r'H:\示例\第6章\书签应用'+name+'.docx',16) 
    myDoc.Close()
wordApp.Quit()




