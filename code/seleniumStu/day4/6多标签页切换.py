# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/24

from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 点击抗击肺炎按钮，这是个超链接
driver.find_element_by_id("virus-2020").click()

# 获得当前所有打开的标签页
all_handle_Sli = driver.window_handles
print(all_handle_Sli)
# 切换到对应的标签页
driver.switch_to.window(all_handle_Sli[1])

# 打印现有确诊人数信息
txt = driver.find_element_by_css_selector(".VirusSummarySix_1-1-264_3wCKWi.VirusSummarySix_1-1-264_123ZxM").text
print(txt)

driver.quit()
