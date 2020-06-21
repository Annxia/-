#在电脑上自动化手机页面，用电脑上的浏览器

from selenium import webdriver

#需要以手机模式打开chrome
options=webdriver.ChromeOptions()
options.add_experimental_option(
    "mobileEmulation",
    {"deviceName": "iPhone X"})

print(options.to_capabilities())
#初始化webdriver
driver=webdriver.Chrome(desired_capabilities=options.to_capabilities())
driver.implicitly_wait(10)
#自动化手机网页了---百度松勤
driver.get('https://www.baidu.com/')

driver.find_element_by_id('index-kw').send_keys('松勤\n')
res=driver.find_element_by_css_selector('[aria-roledescription="搜索结果第1条.标题"]')
if '软件测试-软件测试在线教育领跑者' in res.text:
    print('测试通过')

driver.quit()