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
    'appPackage':'com.hpbr.bosszhipin',
    'appActivity':'.module.launcher.WelcomeActivity',
    #如果被测应用没有安装到手机上,可以指定apk的在电脑上路径
    # 'app':r'D:\apk\xxx.apk',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #如果不想每次都安装UI2驱动，可以这么设置
    # 'skipServerInstallation':True
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#打开通知栏
driver.open_notifications()
time.sleep(6)
#关闭通知栏？
#1.上滑屏幕，2.点击返回按钮 -点击主菜单-home键
KEYCODE_BACK=4
driver.press_keycode(KEYCODE_BACK)

time.sleep(5)

#操作音量
KEYCODE_VOLUME_UP=24
for i in range(5):
    driver.press_keycode(KEYCODE_VOLUME_UP)

driver.quit()
