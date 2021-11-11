# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:06:35 2020

@author: Administrator
"""

import requests,base64,time
APIKey="****************"
SecretKey="****************"
	host = 'https://**************** &client_id='+APIKey+'&client_secret='+SecretKey
response0 = requests.get(host)
dict =response0.json()
access_token=dict["access_token"]
request_url0 = "https://×.×.×.×"
f = open(r’H:\示例\第9章\扫描版PDF_Page4.png', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}
request_url1 = request_url0 + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response1 = requests.post(request_url1, data=params, headers=headers)
request_url2 = "https://×.×.×.×"
params = {"request_id":response1.json()['result'][0]['request_id']}
request_url2 = request_url2 + "?access_token=" + access_token
time.sleep(10)
response2 = requests.post(request_url2, data=params, headers=headers)
url_excel=response2.json()['result']['result_data']
response3=requests.get(url_excel)  
with open(r’H:\示例\第9章\识别结果.xls',"wb") as f: 
    f.write(response3.content)
