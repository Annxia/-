from selenium import webdriver

# 创建一个浏览器驱动对象
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
driver.implicitly_wait(10)
# 访问网址
driver.get("https://www.vmall.com/")
#
# eles = driver.find_elements_by_class_name('category-list')
# for ele in eles:
#     for i in range(10):
#         firstLevel = ele.find_element_by_id('zxnav_{}'.format(i))
#         print("一级菜单：", firstLevel.text)
#         # 鼠标悬浮才出现,冻结页面
#         ActionChains(driver).move_to_element(firstLevel).perform()
#         secondLevels = firstLevel.find_elements_by_xpath('//*[@id="zxnav_{}"]/descendant::li'.format(i))
#
#         for second in secondLevels[:-1]:
#             print("    ", second.text)

print("-------智能家居：新品上市-------")
# 将当前页面滑动到显示区域
driver.execute_script("window.scrollBy(0,900)")
newProducts = driver.find_elements_by_xpath('//*[@id="lc_1098006"]/div/div[2]/div[1]/ul/descendant::li')

for newProduct in newProducts:
    if not newProduct.find_elements_by_tag_name("span"):
        continue
    ele = newProduct.find_elements_by_tag_name("span")
    name = newProduct.find_element_by_xpath('./a//div[@class="grid-title"]')
    price = newProduct.find_element_by_xpath('./a//p[@class="grid-price"]')
    if "新品上市" == ele[0].text:
        print("新品上市：{}, 价格：{}".format(name.text, price.text))


driver.quit()

