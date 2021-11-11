# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:39:29 2020

@author: Administrator
"""
# from myPackage import myModule
from 第2章.myPackage import myModule

p5 = myModule.Person('小李',25,"打球")
p5.speak()
myModule.speak_obj(p5)
p6 = myModule.Kid('小玉',4,"篮球")
myModule.speak_obj(p6)
