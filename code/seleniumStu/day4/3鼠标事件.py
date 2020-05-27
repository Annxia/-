# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/24

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

"""
# 访问网址
driver.get("http://www.baidu.com")
# 定位到要悬停的元素
ele = driver.find_element_by_id("s-usersetting-top")
# 对定位到的元素进行鼠标悬停操作
ActionChains(driver).move_to_element(ele).perform()
"""

driver.get("file:///D:/learn-automated-testing/code/seleniumStu/day4/test1.html")
# 定位到起始元素
startEle = driver.find_element_by_id("blackSquare")
# 定位到目标元素
targetEle = driver.find_element_by_id("targetEle")
# 元素拖拽，将起始元素，拖拽到目标元素
ActionChains(driver).drag_and_drop(startEle, targetEle).perform()

# ele = driver.find_element_by_id("s-usersetting-top")
# ActionChains(driver).context_click(ele).perform()  # 右击
# ActionChains(driver).double_click(ele).perform()  # 双击
# ActionChains(driver).click(ele).perform()  # 单击
