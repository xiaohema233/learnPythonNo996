import multiprocessing
import datetime
import requests
headers={
"Host": "www.ptpress.com.cn",
"Referer": "https://www.ptpress.com.cn/newBook",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
def scraper(url):
    print(url)
    r=requests.get(url,headers=headers)
    fileName=url.replace("https://www.ptpress.com.cn/upload/newbookcatalog/","")
    with open(fileName,"wb") as f: 
        f.write(r.content)  
if __name__ == '__main__':
    multiprocessing.freeze_support()
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
    startTime = datetime.datetime.now()
    with multiprocessing.Pool(2) as p:
        p.map(scraper, urlList)
    print("总耗时：",datetime.datetime.now() - startTime)
