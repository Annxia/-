import time

from selenium import webdriver

driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")
driver.get("https://m.weibo.cn/")

driver.find_element_by_css_selector("#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div").click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div/div[8]/div/div').click()
time.sleep(5)
elements = driver.find_elements_by_class_name('card-list')
time.sleep(5)
# hot = r"https://simg.s.weibo.com/20190429_hot.png"
# new = r"https://simg.s.weibo.com/20190429_new.png"
# fei = r"https://simg.s.weibo.com/20190429_new.png"
# recom = r"https://simg.s.weibo.com/20190429_recom.png"
hotlist = []
newlist = []
feilist = []
recomlist = []
for ele in elements:
    img = ele.find_elements_by_class_name("m-link-icon")
    if img:
        imglink = img[0].find_element_by_tag_name("img")
        src = imglink.get_attribute("src")
        print(src)
        print("hot" in src)
        if "hot" in src:
            hotlist.append(ele.text)
        if "new" in src:
            newlist.append(ele.text)
        if "fei" in src:
            feilist.append(ele.text)
        if "recom" in src:
            recomlist.append(ele.text)

print(hotlist)
print(newlist)
print(feilist)
print(recomlist)



