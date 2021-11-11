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
    import PySimpleGUI as sg
    text0 = sg.Text('输入文件夹 Word')
    text1 = sg.Text('输出文件夹 PDF ')
    text_entry0 = sg.InputText(key='path')
    text_entry1 = sg.InputText(key='outpath')
    ok_btn = sg.Button('开始转换')
    cancel_btn = sg.Button('退出')
    layout = [[text0, text_entry0], [text1, text_entry1], [ok_btn, cancel_btn]]
    window = sg.Window('Word 转 PDF 小工具', layout)
    while True:
        event, values = window.read()
        if event in (None, '退出'):
            break
        if event == '开始转换':
            path = values['path']
            outpath = values['outpath']
            if path == '' or outpath == '':
                sg.popup('请输入文件夹!', text_color='red')
            else:
                doc2pdf(path, outpath)
                sg.popup('转换完毕!')
    window.close()

