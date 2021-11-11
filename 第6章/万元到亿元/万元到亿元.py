# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
from win32com import client
from win32com.client import constants
wordApp =client.DispatchEx('Word.Application')
myDoc=wordApp.Documents.Add(r'H:\示例\第6章\万元到亿元\万元到亿元.doc')
FindA= myDoc.Content.Find
FindA.ClearFormatting
FindA.MatchByte = False
FindA.Forward = True
FindA.Wrap = constants.wdFindStop
FindA.Text = "([0-9,，.]{3,})万元"
FindA.MatchWildcards = True 
listA = []
listB = []
while True:  
    FindA.Execute()
    if FindA.Found == True :
        strA=FindA.Parent.Text
        listA.append(strA)
        x=strA.replace("万元","")
        x=round(float(x)/10000,2)
        listB.append(str(x)+"亿元")
    else:
        break
FindB=myDoc.Content.Find
n=len(listA)
for i in range(n):
    FindB.Text = listA[i]
    FindB.Replacement.Text = listB[i]
    print(listA[i],listB[i])
    FindB.Execute(Replace=2)
myDoc.SaveAs(r'H:\示例\第6章\万元到亿元\万元到亿元_结果.docx')
myDoc.Close()