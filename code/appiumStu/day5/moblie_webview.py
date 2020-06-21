from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "6",
    "deviceName": "test",
    'appActivity': '.MainActivity',
    'appPackage': 'com.example.jcy.wvtest',
    # 设置命令超时时间
    'newCommandTimeout': 6000,
    # 确保自动化之后不重置app
    'noReset': True,
    # 底层驱动
    'automationName': 'UiAutomator2',
    #查看webviwe版本方式2：通过代码的报错来查看
    #指定chromedriver路径
    'chromedriverExecutableDir':'C:\Tools\webdriver\chromedriver_win32_2.23'
    #chromedriver版本匹配地址
    #https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md

}

driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)

#查看当前app的context（appium操作的作用域）
#context-NATIVE_APP的时候-只能操作原生控件
#context-WEBVIEW_包名,只能操作web元素

#查看context的名称
print(driver.contexts)

#当前处于哪个context?
print(driver.current_context)

#如何切换context
driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')

print(driver.current_context)



#访问百度页面
driver.get('http://baidu.com')
#
driver.find_element_by_id('index-kw').send_keys('松勤\n')

#操作原生控件？
driver.switch_to.context('NATIVE_APP')
#点击通知
driver.find_element_by_accessibility_id('通知').click()

input()
driver.quit()

#app的类型
#原生_app
#混合app
#web_app
