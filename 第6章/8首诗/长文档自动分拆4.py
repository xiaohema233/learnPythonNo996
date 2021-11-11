# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
from win32com.client import constants,DispatchEx
wordApp = DispatchEx('Word.Application')
myDoc = wordApp.Documents.Open(r'H:\示例\第6章\8首诗\8首诗_分页符.docx')
docCnt=myDoc.Content
FindA= docCnt.Find
FindA.ClearFormatting
FindA.MatchWildcards = False
FindA.Text = "^m"
i,j = 0,0
while True:  
    FindA.Execute()
    if FindA.Found == True :
        if i>0:
            doc_new = wordApp.Documents.Add()
            s = docCnt.Start
            docRange = myDoc.Range(j, s)
            docRange.Copy()
            doc_new.Content.Paste()
            j = s + 1
            print(str(i))
            doc_new.SaveAs('H:\\示例\\第6章\\8首诗\\1\\'+str(i)+'.docx',16) 
            doc_new.Close()
        i = i + 1
    else:
        break
doc_new = wordApp.Documents.Add()
s = myDoc.Content.End
docRange = myDoc.Range(j, s)
docRange.Copy()
doc_new.Content.Paste()
doc_new.SaveAs('H:\\示例\\第6章\\8首诗\\1\\'+str(i)+'.docx',16) 
doc_new.Close()
myDoc.Close()
wordApp.Quit()
