#导包
import time

from appium import webdriver

old_password=input('请输入原密码：')
new_password=input('请输入新密码：')


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
    #指定自动化驱动
    'automationName':'UiAutomator2',
    # 'skipServerInstallation':True
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

# 1.进入我的标签
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()
# 2.点击右上角设置图标
driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
# 3.进入账号与绑定
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.widget.LinearLayout[1]/android.view.ViewGroup').click()
time.sleep(1)
# 4.进入设置密码
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.widget.LinearLayout[2]/android.view.ViewGroup').click()
# 5.完成密码设置
# print(driver.page_source)
#5.1输入旧密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(old_password)
#5.2设置新密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(new_password)
#5.3确认密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(new_password)
#5.5点击修改密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()
time.sleep(5)
#选择账号密码登录
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()

#使用新密码登录
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(new_password)

driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()

#验证登录进来之后有职位标签
job_tag=driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_tab_1')

assert job_tag.text=='职位'

driver.quit()
