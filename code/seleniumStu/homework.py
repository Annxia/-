from selenium import webdriver

driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://m.weibo.cn/")
driver.find_element_by_class_name("m-text-cut").click()

driver.find_element_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4').click()

elements = driver.find_elements_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div')

for ele in elements:
    icon = ele.find_elements_by_class_name("m-link-icon")
    if icon:
        img = icon[0].find_element_by_tag_name("img")
        if "hot" in img.get_attribute("src"):
            print('热    {}'.format(ele.find_element_by_class_name("m-text-cut").text))
        elif "new" in img.get_attribute("src"):
            print('新    {}'.format(ele.find_element_by_class_name("m-text-cut").text))
        elif "fei" in img.get_attribute("src"):
            print('沸    {}'.format(ele.find_element_by_class_name("m-text-cut").text))
        elif "recom" in img.get_attribute("src"):
            print('荐    {}'.format(ele.find_element_by_class_name("m-text-cut").text))

driver.quit()