# -*- coding: utf-8 -*-

import xlwings as xw
@xw.sub
def cell(i,row,col,value):
	wb=xw.Book.caller()
	ws=wb.sheets[i]
	ws.range(row,col).value=value
@xw.func
def add(a,b):
	return a+b
