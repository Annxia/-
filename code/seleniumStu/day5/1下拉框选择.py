
from selenium import webdriver
from selenium.webdriver.support.select import Select

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get("file:///D:/learn-automated-testing/code/seleniumStu/day5/test.html")

# 定位到下拉框元素
ele = driver.find_element_by_id("abc")

# 根据下拉框文本来选择
# Select(ele).select_by_visible_text("月薪三万")

# 根据value属性选择
Select(ele).select_by_value("p2")

driver.quit()