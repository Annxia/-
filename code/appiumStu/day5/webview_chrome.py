from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'platformVersion':'10',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #直接指定浏览器名称参数为chrome--无需写包名和入口信息
    'browserName':'Chrome',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #如果不想每次都安装UI2驱动，可以这么设置
    #指定自动化驱动
    'automationName':'UiAutomator1',
    'unicodeKeyboard':True,
    'resetKeyboard':True,
    'skipServerInstallation':True,
    #使用指定的浏览器驱动-匹配手机上的谷歌浏览器
    'chromedriverExecutableDir':r'E:\webdriver\chromedriver_81.0.4044.138'

}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#操作浏览器内容，接下里可以完全使用selenium的方式去自动化页面

#自动化手机网页了---百度松勤
driver.get('https://www.baidu.com/')

driver.find_element_by_id('index-kw').send_keys('松勤\n')
res=driver.find_element_by_css_selector('[aria-roledescription="搜索结果第1条.标题"]')
if '软件测试-软件测试在线教育领跑者' in res.text:
    print('测试通过')


driver.quit()

