# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:00:56 2020

@author: Administrator
"""
import time
from pywinauto.application import Application
program_path = r'C:\Program Files (x86)\ABBYY FineReader 12\FineReader.exe'
app = Application().start(program_path) 
dlg = app.window(title_re ='ABBYY FineReader 12 Professional')
dlg.wait('visible')
dlg.type_keys('^O')
time.sleep(2)
from pynput import keyboard
k = keyboard.Controller()
k.type(r'H:\示例\第10章\扫描版PDF.pdf')
time.sleep(1)
from pynput.keyboard import Key
k.press(Key.enter)
k.release(Key.enter)
time.sleep(20)
dlg1=app['无标题文档 [1] - ABBYY FineReader 12 Professional']
dlg1.type_keys('%F')
time.sleep(1)
k.press('V')
k.press('P')
time.sleep(1)
k.release('P')
k.release('V')
time.sleep(1)
k.type(r'H:\示例\第10章\扫描版PDF_OCR.pdf')
time.sleep(1)
k.press(Key.enter)
k.release(Key.enter)
time.sleep(10)
dlg1.type_keys('^W')
time.sleep(1)
k.press('N')
time.sleep(1)
k.release('N')
