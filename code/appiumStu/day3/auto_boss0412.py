#导包
from appium import webdriver

#准备自动化配置信息
caps={
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

#初始化webdriver
driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
driver.implicitly_wait(10)

#选择元素操作元素

#点击放大镜
# eles=driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')
# eles[1].click()
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/*').click()

#输入岗位信息
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search').send_keys('自动化测试')

#选择第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()


#点击第一个岗位
driver.find_element_by_id('com.hpbr.bosszhipin:id/view_job_card').click()

##获取地区 工作年限 学历
location=driver.find_element_by_id('tv_required_location').text
work_exp=driver.find_element_by_id('tv_required_work_exp').text
degree=driver.find_element_by_id('tv_required_degree').text

print(f'地区：{location}|工作年限：{work_exp}|学历{degree}')


#演示XPATH语法
#根据ID选择
jobname=driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/tv_job_name"]').text
print(jobname)


driver.quit()


