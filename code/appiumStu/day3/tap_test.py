#导包
import time

from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.alpha.lagouapk',
    'appActivity':'.HelloActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #指定自动化驱动
    'automationName':'UiAutomator1',

}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

# time.sleep(5)
#定位首页出现的元素
driver.find_element_by_id('com.alpha.lagouapk:id/iv_banner_content_pic')
#计算屏幕高度和宽度
win_size=driver.get_window_size()
width=win_size['width']
height=win_size['height']
#通过比例得出近似的坐标
x=width/2
y=height/16


#通过坐标点击输入框
driver.tap([(x,y)])

#click是用元素对象的方法

#设置手指停留时间---模拟长按效果


input('输入任意键退出代码')
driver.quit()


