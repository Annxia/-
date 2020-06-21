from appium import webdriver
#appium1.15版本有bug，无法成功切换webview
#推荐使用1.13版本


#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'9',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #包名--入口信息com.example.haiwen.myhybirdapp/.MainActivity
    'appPackage':'com.example.haiwen.myhybirdapp',
    'appActivity':'.MainActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #如果不想每次都安装UI2驱动，可以这么设置
    #指定自动化驱动
    'automationName':'UiAutomator2',
    'skipServerInstallation':True,
    #使用指定的浏览器驱动-匹配手机上的谷歌浏览器
    'chromedriverExecutableDir':r'C:\Tools\webdriver\chromedriver_win32_v80'
}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#输入豆瓣手机端网页
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/editText').send_keys('https://m.douban.com/home_guide')
driver.find_element_by_id('com.example.haiwen.myhybirdapp:id/button').click()

#查看当前app的context
print(driver.contexts)

#查看当前的app处于哪个context
print(driver.current_context)

#切换context以操作网页
driver.switch_to.context('WEBVIEW_com.example.haiwen.myhybirdapp')

print(driver.current_context)

#自动化网页-搜索电影-查看电影评分
driver.find_element_by_css_selector('.search-input').send_keys('肖申克的救赎\n')

#获取电影评分
rate=driver.find_element_by_css_selector('li.search-module:nth-child(1) .search_results_subjects li:nth-child(1) .rating>span:nth-child(2)').text

print(f'评分是{rate}')

driver.quit()
