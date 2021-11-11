from pywinauto import Application 
app = Application().start('notepad.exe') 
app['无标题-记事本'].Edit.type_keys('明了胜于晦涩\n', with_newlines=True) 
app['无标题-记事本'].Edit.type_keys('优美胜于丑陋') 
app['无标题-记事本'].menu_select('文件(F)->保存(S)') 
app['另存为']['Edit'].type_keys("示例")
app['另存为']['保存(S)'].double_click()
app['示例.txt-记事本'].close()
