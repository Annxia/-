from selenium import webdriver
# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get("http://www.baidu.com")

# 截屏，截取整个页面
driver.get_screenshot_as_file("./all.png")

# 截屏，截取某个特定元素
ele = driver.find_element_by_id("kw")
ele.screenshot("./ele.png")

driver.quit()