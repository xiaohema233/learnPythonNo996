import time
from selenium import webdriver
from pynput.keyboard import Key, Controller
driver = webdriver.Chrome(r"H:\示例\第10章\chromedriver.exe")
RequestURL='https://www.ptpress.com.cn/p/news/1589965248338.html'
driver.get(RequestURL)
time.sleep(5)
k = Controller()
with k.pressed(Key.ctrl):
    k.press("p");k.release("p")
time.sleep(5)
k.press(Key.enter);k.release(Key.enter);time.sleep(5)
k.type('另类爬虫');time.sleep(5)
k.press(Key.enter);k.release(Key.enter);time.sleep(10)
driver.close()
driver.quit()
