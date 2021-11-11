import datetime
import threading,queue
import requests
headers={
"Host": "www.ptpress.com.cn",
"Referer": "https://www.ptpress.com.cn/newBook",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
urlList=[   
"https://www.ptpress.com.cn/upload/newbookcatalog/20200517新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200510新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200503新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200426新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200419新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200412新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200405新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200322新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200315新书目录.xls",
"https://www.ptpress.com.cn/upload/newbookcatalog/20200308新书目录.xls"]
class myThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while not self.queue.empty():
            url = self.queue.get()
            r=requests.get(url,headers=headers)
            fileName=url.replace("https://www.ptpress.com.cn/upload/newbookcatalog/","")
            with open('xls/'+fileName,"wb") as f: 
                f.write(r.content)  
            self.queue.task_done()
startTime = datetime.datetime.now()
queue = queue.Queue()
for url in urlList:
    queue.put(url)
for i in range(5):
    thread  = myThread(queue)
    thread .setDaemon(True)
    thread .start()
queue.join()
print("总耗时：",datetime.datetime.now() - startTime)
