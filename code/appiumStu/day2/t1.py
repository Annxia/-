#导包
import time

from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.example.jcy.wvtest',
    'appActivity':'.MainActivity',
    #如果被测应用没有安装到手机上,可以指定apk的在电脑上路径
    # 'app':r'D:\apk\xxx.apk',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#通过content-desc 也就是accessibility id获取元素

driver.find_element_by_accessibility_id('面板').click()

time.sleep(3)


driver.find_element_by_accessibility_id('通知').click()
time.sleep(3)

#输入姓名
driver.find_element_by_accessibility_id('unique name').send_keys('小星')


time.sleep(5)
driver.quit()

