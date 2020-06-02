from pprint import pprint

from selenium import webdriver
from selenium.webdriver.support.select import Select

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get("http://127.0.0.1:8088/login")

input(">>>")

# 获取cookie信息
cook = driver.get_cookies()

# 将获取的cookie信息打印
for cookDic in cook:
    pprint(cookDic)

driver.quit()