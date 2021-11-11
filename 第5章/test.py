# -*- coding: utf-8 -*-
 
import xlwings as xw
 
 
def say_hi():
    
    wb = xw.Book.caller()
    sht = wb.sheets[0]
    sht.range('A1').value = 'Hello, world'


import xlwings as xw
@xw.sub
def cell(i,row,col,value)
	wb=xw.Book.caller()
	ws=wb.sheets[i]
	ws.range((r,c)).value=v
@xw.func
def add(a,b)
	return a+b
import xlwings as xw
import os
@xw.func
def cwf():
    return os.getcwd()