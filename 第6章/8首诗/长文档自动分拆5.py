# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
from win32com.client import constants,DispatchEx
wordApp = DispatchEx('Word.Application')
myDoc = wordApp.Documents.Open(r'H:\示例\第6章\8首诗\1\1.docx')
selection = wordApp.Selection
selection.HomeKey(Unit=constants.wdStory)
selection.EndKey(Unit=constants.wdLine, Extend=constants.wdExtend)
selection.Delete()
myDoc.Save()
myDoc.Close()

