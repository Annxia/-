
from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
# 访问网址
driver.get(r"file:\D:\learn-automated-testing\code\seleniumStu\day1\test1.html")

# 匹配元素列表，返回所有匹配到的元素列表，如果一个也匹配不到，就返回空列表
# id 属性是惟一的
eleSli = driver.find_elements_by_tag_name("p")

# for ele in eleSli:
#     print(ele.text)

print(eleSli[3].text)
print(eleSli[-1].text)

driver.quit()
