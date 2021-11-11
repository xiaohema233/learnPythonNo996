# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
from win32com.client import constants,DispatchEx
wordApp = DispatchEx('Word.Application')
wordApp.Visible=1
wordApp.DisplayAlerts=0
with open(r'H:\示例\第6章\公文格式自动设置.txt') as f:
    text=f.read()
myDoc=wordApp.Documents.Add()
myDoc.Range(0,0).InsertBefore(text)
CentimetersToPoints=28.35
myDoc.PageSetup.PageWidth=CentimetersToPoints * 21
myDoc.PageSetup.PageHeight=CentimetersToPoints * 29.7
myDoc.PageSetup.TopMargin=CentimetersToPoints * 3.7
myDoc.PageSetup.BottomMargin=CentimetersToPoints * 3.5
myDoc.PageSetup.LeftMargin=CentimetersToPoints * 2.8
myDoc.PageSetup.RightMargin=CentimetersToPoints * 2.6
myDoc.PageSetup.LinesPage=22
myDoc.Content.Font.NameFarEast="仿宋_GB2312"
myDoc.Content.Font.Size=15.75
Start=myDoc.Paragraphs(2).Range.Start
End=myDoc.Paragraphs(myDoc.Paragraphs.Count).Range.End
myRange=myDoc.Range(Start,End)
myRange.ParagraphFormat.CharacterUnitFirstLineIndent=2
myDoc.Paragraphs(1).Range.Font.NameFarEast="方正小标宋简体"
myDoc.Paragraphs(1).Range.Font.Size=21
myDoc.Paragraphs(1).Range.Font.Bold=True
myDoc.Paragraphs(1).Range.ParagraphFormat.Alignment=1
FindA=myDoc.Content.Find
FindA.ClearFormatting
FindA.MatchWildcards=True
FindA.Replacement.ClearFormatting
FindA.Replacement.Font.NameFarEast="黑体"
FindA.Replacement.Font.Bold=True
FindText="[一二三四五六七八九十]@、*^13"
FindA.Execute(FindText,ReplaceWith="",Format=True,Replace=2)
FindA.Replacement.Font.NameFarEast="楷体_GB2312"
FindA.Replacement.Font.Bold=True
FindText="（[一二三四五六七八九十]@）*^13"
FindA.Execute(FindText,ReplaceWith="",Format=True,Replace=2)
FindA.Replacement.Font.NameFarEast="仿宋_GB2312"
FindA.Replacement.Font.Bold=True
FindA.Execute(FindText="[0-9]@、*^13",ReplaceWith="",Format=True,Replace=2)
FindA.Execute(FindText="（[0-9]@）*^13",ReplaceWith="",Format=True,Replace=2)
FindText="[一二三四五六七八九十]@是"
FindA.Execute(FindText,ReplaceWith="",Format=True,Replace=2)
myDoc.Sections(1).Footers(1).PageNumbers.Add(PageNumberAlignment=4)
myDoc.Sections(1).Footers(1).Range.Select()
pageNum=wordApp.Selection
pageNum.MoveLeft(constants.wdCharacter,2)
pageNum.TypeText("—")
pageNum.MoveRight(constants.wdCharacter,1)
pageNum.TypeText("—")
pageNum.WholeStory()
pageNum.Font.Name="宋体"
pageNum.Font.Size=14
myDoc.Sections(1).Headers(1).Range.ParagraphFormat.Borders(-3).LineStyle=0
myDoc.SaveAs(r'H:\示例\第6章\公文格式自动设置_结果.docx')
myDoc.Close()
wordApp.Quit()
