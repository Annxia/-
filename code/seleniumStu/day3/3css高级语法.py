
"""
css selector

1、css 配合 HTML 工作，它实现的原理是匹配对象的原理
    而xpath 是配合xml工作的，xpath实现的原理是遍历
    css 的性能更加优秀
2、相对于 xpath css的语法更加简洁明了
3、前端开发主要用的都是css，不使用xpath
"""

from selenium import webdriver
import time

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
driver.get("https://tieba.baidu.com/index.html")

# 向右滚动100， 向下滚动500
driver.execute_script("window.scrollBy(100, 500)")

# driver.quit()
