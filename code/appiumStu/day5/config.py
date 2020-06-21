boss_caps={
    #平台
    "platformName": "Android",
    "platformVersion": "8",
    "deviceName": "test",
    #被测app的信息
    'appActivity':'.module.launcher.WelcomeActivity',
    'appPackage':'com.hpbr.bosszhipin',
    #设置命令超时时间
    'newCommandTimeout':6000,
    #确保自动化之后不重置app
    'noReset':True,
    #底层驱动
    'automationName':'UiAutomator2',
    #如果不想每次都安装UI2驱动，可以这么设置
    'skipServerInstallation':True,
}