from selenium import webdriver
import win32com.client
# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get("http://tinypng.com/")

# 对于input实现的上传功能，通过 sendkeys 指定本地文件路径即可实现上传

win32com.client
