import requests, json,re,time
from selenium import webdriver
driver1 = webdriver.Chrome(r"H:\示例\第4章\chromedriver.exe")
driver1.get("https://×.×.×.×")
time.sleep(3)
driver1.save_screenshot('百度1.png')
time.sleep(30)
Cookies1 = driver1.get_cookies()
jsonCookies = json.dumps(Cookies1)
with open('cookies.txt', 'w') as f:
   f.write(jsonCookies)
driver1.quit()
driver2 = webdriver.Chrome(r"H:\示例\第4章\chromedriver.exe")
driver2.get("https://×.×.×.×")
driver2.delete_all_cookies()
with open('cookies.txt', 'r', encoding='utf8') as f:
	Cookies = json.loads(f.read())
for cookie in Cookies:
	if 'expiry' in cookie:
		del cookie['expiry']
	driver2.add_cookie(cookie)
driver2.refresh()
time.sleep(3)
driver2.save_screenshot('百度2.png')
driver2.quit()
Cookies3 = {}
for cookie in Cookies1:
	Cookies3[cookie['name']] = cookie['value']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
r = requests.get("https://×.×.×.×", headers=headers, cookies=Cookies3)
m=re.findall('[\u4e00-\u9fa5]',r.text)
print("".join(m))
