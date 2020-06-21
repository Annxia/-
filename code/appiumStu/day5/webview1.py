#下载apk安装包
#使用命令 adb install wv_test.apk  安装到手机上
#使用代码完成以下操作
#1.输入豆瓣手机端网址--https://m.douban.com/home_guide
#2.按下enter键访问手机端页面
#3.切到webview中-网页操作模式
#4.使用网页中的搜索框搜索肖申克救赎
#5.在结果中获取电影评分

# coding=utf8
from appium import webdriver
import time
import traceback
 
desired_caps = {
    'automationName': 'UiAutomator2',
    'skipServerInstallation':True,
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'test',
    'appPackage': 'com.example.haiwen.myhybirdapp',
    'appActivity': '.MainActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard':True,
    'chromedriverExecutableDir':r'C:\Tools\webdriver\chromedriver_win32_v80',#选择符合webview版本的谷歌驱动
    'noReset': True,
    'newCommandTimeout': 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

#输入URL
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/editText').send_keys('https://m.douban.com/home_guide')

driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/button').click()
time.sleep(3)
#操作原始应用里的webview
try:
    # -----------------------
    print(driver.current_context)
    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.example.haiwen.myhybirdapp')
    #搜索电影肖申克救赎
    driver.find_element_by_css_selector('.search-input').send_keys('肖申克救赎\n')
    #获取评分
    rate=driver.find_element_by_css_selector('li.search-module:nth-child(1) .search_results_subjects li:nth-child(1) .rating>span:nth-child(2)').text
    print(f'评分是{rate}')

    # -----------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()