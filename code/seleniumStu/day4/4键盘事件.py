# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/24

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 定位到输入框
inpEle = driver.find_element_by_id("kw")
inpEle.send_keys("selenium")
time.sleep(2)

inpEle.send_keys(Keys.F12)

# # 删除最后一个字母
# inpEle.send_keys(Keys.BACK_SPACE)

# # 输入空格
# inpEle.send_keys(Keys.SPACE)
# inpEle.send_keys("安装")

# # Ctrl + a 全选输入框内容
# inpEle.send_keys(Keys.CONTROL, "a")
# # Ctrl + x 剪切输入框内容
# inpEle.send_keys(Keys.CONTROL, "x")


# Keys.SPACE  空格键
# Keys.ENTER 回车键
# Keys.ESCAPE esc按键
# Keys.F12
