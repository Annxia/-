from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

# 用于获取当前页面的标题
print(driver.title)

# 用户获得当前页面的url
print(driver.current_url)

# 获取**标签对**之间的文本信息,如果标签对之间没有文本信息，打印出来为空
# 也可以获取子标签对之间的文本信息
ele = driver.find_element_by_class_name("title-text")
print(ele.text)

driver.quit()