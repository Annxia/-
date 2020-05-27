
from selenium import webdriver
import time

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

driver.get("http://news.baidu.com")

# 浏览器后退
driver.back()
time.sleep(2)

# 浏览器前进
driver.forward()
time.sleep(2)

# 刷新界面
driver.refresh()
time.sleep(2)



"""
# # 参数数字为像素点
# print("设置浏览器宽600， 高600 显示")
# driver.set_window_size(600, 600)
# time.sleep(2)
# 
# # 设置为全屏显示
# driver.maximize_window()
# time.sleep(2)
# 
# # 设置最小化
# driver.minimize_window()
# time.sleep(2)
"""



driver.quit()
