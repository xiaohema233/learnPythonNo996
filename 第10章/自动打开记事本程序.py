import win32api,win32gui,win32con,time
win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1) 
time.sleep(1)
hwnd = win32gui.FindWindow(None, u"无标题 - 记事本")
win32gui.SetForegroundWindow(hwnd)
win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE, 0)
