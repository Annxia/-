# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/18

from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 找到搜索文本框
input_element = driver.find_element_by_id("kw")
# 向文本框输入内容
input_element.send_keys("python")
# 找到搜索按钮
search_element = driver.find_element_by_id("su")
# 点击搜索按钮
search_element.click()

# 退出浏览器
driver.quit()
