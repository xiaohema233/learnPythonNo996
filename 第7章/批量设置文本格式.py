# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""
from win32com.client import Dispatch
pptApp=Dispatch('PowerPoint.Application')
prt=pptApp.Presentations.Open(r'H:\示例\第7章\hello1_txt.pptx')
for sld in prt.Slides:
    for shp in sld.Shapes:
        if shp.HasTextFrame:
            font=shp.TextFrame.TextRange.Font
            font.NameAscii = "微软雅黑" 
            font.NameFarEast = "微软雅黑" 
            font.Name= "微软雅黑" 
            font.Size = 20                                        
            font.Color.RGB = 0
            font.Subscript = 0
            font.Superscript = 0
            font.Underline = 0 
            font.Bold = 0  
            font.Italic = 0   
            font.Underline=0 
prt.SaveAs(r'H:\示例\第7章\hello1_txt1.pptx')
prt.Close()
pptApp.Quit()
