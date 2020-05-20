'''
xpath 使用路径表达式来选取 HTML 文档中的节点或节点集
'''
from selenium import webdriver
# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get(r"file:\D:\learn-automated-testing\code\seleniumStu\day2\test.html")


# driver.quit()