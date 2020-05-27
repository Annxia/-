# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/24

from selenium import webdriver
import time

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("file:///D:/learn-automated-testing/code/seleniumStu/day4/test.html")

"""
# 触发对话框
driver.find_element_by_id("bu1").click()
# 获取对话框
al = driver.switch_to.alert
# 确认对话框
al.accept()
"""

"""
# 触发确认框
driver.find_element_by_id("bu2").click()
# 获取确认框
al = driver.switch_to.alert
al.accept()  # 点击确认
# 再次触发确认框
driver.find_element_by_id("bu2").click()
al.dismiss()  # 点击取消
"""

# 触发提示框
driver.find_element_by_id("bu3").click()
# 获取提示框
al = driver.switch_to.alert
# 向提示框中输入内容
al.send_keys("哈哈")
time.sleep(5)
al.accept()

time.sleep(5)
driver.quit()
