import datetime
import requests
headers={
"Host": "www.ptpress.com.cn",
"Referer": "https://www.ptpress.com.cn/newBook",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
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
"https://www.ptpress.com.cn/upload/newbookcatalog/20200308新书目录.xls"
        ]
def scraper(url):
    startTime = datetime.datetime.now()
    fileName=url.replace("https://www.ptpress.com.cn/upload/newbookcatalog/","")
    r=requests.get(url,headers=headers)
    print(fileName+" 请求耗时：",datetime.datetime.now() - startTime)
    startTime = datetime.datetime.now()
    with open('xls/'+fileName,"wb") as f: 
        f.write(r.content)  
    print(fileName+" 写入耗时：",datetime.datetime.now() - startTime)
startTime0 = datetime.datetime.now()
for url in urlList:
    scraper(url)
print("总耗时：",datetime.datetime.now() - startTime0) 
