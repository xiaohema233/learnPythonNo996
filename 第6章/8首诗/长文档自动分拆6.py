# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
import os
from win32com.client import constants,DispatchEx
wordApp = DispatchEx('Word.Application')
path = 'H:\\示例\\第6章\\8首诗\\1\\'
files=os.listdir(path)
print(files)
for file in files:
    myDoc = wordApp.Documents.Open(path+file)
    selection = wordApp.Selection
    selection.HomeKey(Unit=constants.wdStory)
    selection.EndKey(Unit=constants.wdLine, Extend=constants.wdExtend)
    txt=selection.Text
    myDoc.Close()
    new_name=path+txt.strip()+".docx"
    os.rename(path+file, new_name)
wordApp.Quit()
