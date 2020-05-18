# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/18
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get(r"file:\D:\learn-automated-testing\code\seleniumStu\day1\test1.html")

# 元素定位的另一种方式，为po模式做准备
ele = driver.find_element(By.ID, "abc")
print(ele.text)
# 获取元素的属性值
print(ele.get_attribute("href"))

ele = driver.find_element(By.CLASS_NAME, "abd")
print(ele.get_attribute("title"))

driver.quit()
