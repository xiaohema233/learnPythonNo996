import time
from pywinauto.application import Application
program_path = r"C:\Program Files (x86)\Sursen\Reader\SursenReader.exe"
app = Application().start(program_path) 
dlg = app.window(title_re ='书生阅读器')
dlg.wait('visible')
dlg_0=dlg["文件BCGPToolBar:400000:8:10003:10"]
dlg_0.click(button='left', coords=(20, 10)) 
dlg_1 = app.window(title_re ='打开')
dlg_1.wait('visible')
file=r"H:\示例\第10章\案例文件.gd"
app['打开'].Edit.type_keys(file)
dlg_2=dlg_1["打开Button"]
dlg_2.double_click(button='left', coords=(3, 3))
dlg = app.window(title_re='书生阅读器')
dlg_3=dlg["文件BCGPToolBar:400000:8:10003:10"]
dlg_3.click(button='left', coords=(70, 10))
dlg_4 = app.window(title_re='打印')
dlg_4.wait('visible')
dlg_4.ComboBox.Select("Adobe PDF")
dlg_5=dlg_4["确定Button"]
dlg_5.double_click(button='left', coords=(3, 3))
time.sleep(2)
app = Application().connect(title_re="另存 PDF 文件为")
dlg_6 = app.window(title_re='另存 PDF 文件为')
app['另存 PDF 文件为'].Edit.type_keys("PDF版本案例文件")
dlg_7=dlg_6["保存Button"]
dlg_7.double_click(button='left', coords=(3, 3))
time.sleep(8)
app = Application().connect(title_re="书生阅读器")
dlg_8 = app.window(title_re='书生阅读器')
dlg_8.type_keys('%F')
time.sleep(2)
import win32api,win32con
win32api.keybd_event(0x43,0,0,0)  
win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)  

