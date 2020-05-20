

from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get(r"file:\D:\learn-automated-testing\code\seleniumStu\day1\test.html")

"""
# 通过id属性定位, 只返回匹配到的第一个元素，如果找不到，就报错
textElment = driver.find_element_by_id("abd")
# 获取元素文本值
print("获取到元素的文本值:", textElment.text)
"""

"""
# 通过name属性定位, 只返回匹配到的第一个元素，如果找不到，就报错
inp_element = driver.find_element_by_name("a1")
inp_element.send_keys("孔雀东南飞")
"""

"""
# 元素定位第三招
# 通过 xpath 定位, 只返回匹配到的第一个元素，如果找不到，就报错
option_element = driver.find_element_by_xpath("/html/body/div/select/option[2]")
print("xpath定位", option_element.text)
option_element.click()
"""

"""
# 元素定位第四招
# 通过链接文本定位, 只返回匹配到的第一个元素，如果找不到，就报错
driver.find_element_by_link_text("访问百度").click()
"""

"""
# 元素定位的第五种方法
# 通过部分链接文本文本定位, 只返回匹配到的第一个元素，如果找不到，就报错
driver.find_element_by_partial_link_text("访").click()
"""

"""
# 元素定位的第六种方法
# 通过标签名称进行匹配查找, 只返回匹配到的第一个元素，如果找不到，就报错
ele = driver.find_element_by_tag_name("span")
print(ele.text)
"""

"""
# 元素定位的第七种方法
# 根据 class 名称进行查找, 只返回匹配到的第一个元素，如果找不到，就报错
# class是复合类，具有多个属性值，任选其中一个就可以，不可以有空格
ele = driver.find_element_by_class_name("a2")
print(ele.text)
"""

# 元素定位的第八种方法
# 通过 css 选择器查找, 只返回匹配到的第一个元素，如果找不到，就报错
ele = driver.find_element_by_css_selector("body > div:nth-child(7) > table > tbody > tr:nth-child(2) > td")
print(ele.text)

driver.quit()
