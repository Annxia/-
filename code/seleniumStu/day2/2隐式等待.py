import time

from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 设置隐式等待,设置一次全局有效  优点：简单  缺点：浪费时间,同一页面不刷新时仍要隐式等待
driver.implicitly_wait(10)
# 访问网址
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("松勤\n")

# time.sleep(1)
driver.find_element_by_link_text("松勤软件测试_腾讯课堂").click()

driver.quit()