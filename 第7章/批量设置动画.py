# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:33:17 2020

@author: Administrator
"""
from win32com.client import Dispatch, constants
pptApp = Dispatch('PowerPoint.Application')
prt=pptApp.Presentations.Open(r'H:\示例\第7章\Hello1.pptx ',False,False,False)
for slide in prt.Slides:
    settings=slide.Shapes(1).AnimationSettings
    settings.AdvanceMode = constants.ppAdvanceOnTime
    settings.AdvanceTime = 0
    settings.EntryEffect = constants.ppEffectFlyFromLeft
prt.SaveAs(r'H:\示例\第7章\Hello1_settings.pptx')
prt.Close()
pptApp.Quit()

