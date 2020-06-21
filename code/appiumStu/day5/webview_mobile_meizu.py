# coding=utf8
from appium import webdriver
import time
import traceback
 
desired_caps = {
    # 'automationName': 'UiAutomator1',
    'platformName': 'Android',
    'platformVersion': '8',
    'deviceName': 'test',
    'browserName':'Chrome',
    'chromedriverExecutableDir':r'C:\Tools\webdriver\chromedriver_win32_2.37',
    'newCommandTimeout': 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(20)
#启动手机里的浏览器
try:

    driver.implicitly_wait(10.0)
    driver.get('http://www.baidu.com')
    print(driver.contexts)
    print(driver.current_context)
    # 如果出现定位弹出框，需要切换到原生部分点击按钮
    driver.switch_to.context('NATIVE_APP')
    driver.find_element_by_id('com.android.chrome:id/negative_button').click()

    driver.switch_to.context('CHROMIUM')
    time.sleep(1)
    driver.find_element_by_id('index-kw').send_keys('松勤\n')

    # driver.find_element_by_id('index-bn').click()
    time.sleep(3)


except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()