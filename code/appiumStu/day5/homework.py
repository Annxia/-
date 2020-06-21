import time

from appium import webdriver

#准备自动化配置信息

#准备自动化配置信息

desired_caps = {
    'automationName': 'UiAutomator1',
    'unicodeKeyboard':True,
    'resetKeyboard':True,
    'skipServerInstallation':True,
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'test',
    'appPackage': 'com.example.haiwen.myhybirdapp',
    'appActivity': '.MainActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard':True,
    'chromedriverExecutableDir':r'E:\webdriver\chromedriver_79',
    'noReset': True,
    'newCommandTimeout': 6000
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

# 输入URL
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/editText').send_keys('https://m.douban.com/home_guide')
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/button').click()
time.sleep(3)
# 查看当前的app处于哪个context
print(driver.current_context)
# 切换到网页模式
print("打印contexts",driver.contexts)
# driver.switch_to.context('WEBVIEW_com.example.haiwen.myhybirdapp')
driver.switch_to.context('WEBVIEW_com.example.haiwen.myhybirdapp')
print(driver.current_context)
#搜索电影肖申克救赎
driver.find_element_by_css_selector('.search-input').send_keys('肖申克救赎\n')
#获取评分
rate=driver.find_element_by_css_selector('li.search-module:nth-child(1) .search_results_subjects li:nth-child(1) .rating>span:nth-child(2)').text
print(f'评分是{rate}')
