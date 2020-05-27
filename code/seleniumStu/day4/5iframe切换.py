# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/24


from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("D:/learn-automated-testing/code/seleniumStu/day4/test2.html")

# 第一部曲：定位到需要切换进去的iframe
iframeEle = driver.find_element_by_css_selector("iframe")
# 第二部曲：切换进入刚才找到的元素
driver.switch_to.frame(iframeEle)
# 第三部曲：开始你的表演
driver.find_element_by_id("kw").send_keys("123\n")

# 切换回原来的主页面，也就是最外层
driver.switch_to.default_content()
driver.find_element_by_id("abc").send_keys("这是外层的input")
