from appium import webdriver

caps={
#平台
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "test",
    #被测app信息-仅限chrome浏览器
    'browserName':'Chrome',
    'newCommandTimeout':6000,
     #确保自动化之后不重置app
    'noReset':True,
     #底层驱动
    'automationName':'UiAutomator2',
    #指定chromedriver
    'chromedriverExecutableDir':'C:\Tools\webdriver\chromedriver_win32_v81'

}

driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)

#访问百度页面
driver.get('http://baidu.com')

driver.find_element_by_id('index-kw').send_keys('松勤\n')

input()

driver.quit()


