# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
from win32com.client import constants,DispatchEx
wordApp = DispatchEx('Word.Application')
myDoc = wordApp.Documents.Open(r'H:\示例\第6章\8首诗\8首诗.docx')
FindA= myDoc.Content.Find
FindA.ClearFormatting
FindA.MatchByte = False
FindA.Forward = True
FindA.Wrap = constants.wdFindStop
FindA.Text = "第[0-9]{1,3}首*^13"
FindA.MatchWildcards = True 
FindA.Replacement.ClearFormatting
FindA.Replacement.Style = myDoc.Styles("标题 1")
FindA.Replacement.ParagraphFormat.Alignment = 1
FindA.Execute(ReplaceWith ="", Format =True, Replace =2)
myDoc.SaveAs(r'H:\示例\第6章\8首诗\8首诗2.docx',16) 
myDoc.Close()
wordApp.Quit()  
