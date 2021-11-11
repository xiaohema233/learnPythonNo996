# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:37:19 2020

@author: Administrator
"""

import os,fnmatch
from win32com import client
def doc2pdf(path,outpath):
    if os.path.exists(outpath)==False: 
    	os.makedirs(outpath)
    wordApp=client.DispatchEx('Word.Application')
    for foldName, subfolders, filenames in os.walk(path):    
    	for filename in filenames: 
    		if fnmatch.fnmatch(filename,"*.doc*"):
    			myDoc = wordApp.Documents.Open(path+"\\"+filename)
    			myDoc.SaveAs (outpath+"\\"+filename.split(".")[0]+'.pdf',17)
    			myDoc.Close()
    wordApp.Quit()
if __name__ == '__main__':
    import sys
    doc2pdf(sys.argv[1], sys.argv[2])
#    doc2pdf(input("输入文件夹WORD:"), input("输出文件夹PDF:"))
