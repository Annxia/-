#导包
from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息:
    #adb shell dumpsys activity recents | findstr intent={
    'appPackage':'com.hpbr.bosszhipin',
    'appActivity':'.module.launcher.WelcomeActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    # 'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
    #如果需要输入中文，并且用的是UI1驱动，需要设置输入法
    # 'unicodeKeyboard':True,
    # 'resetKeyboard':True
}
#启动被测应用
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(15)

#点击放大镜
driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')[1].click()

#点击输入框
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search').click()

#输入软件测试
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search').send_keys('自动化测试')

#选择第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/rl_words').click()

#进入职位搜索界面-输出职位信息--名称，薪资，公司
job_cards=driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

for job_card in job_cards:
    #职位名
    job_name=job_card.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name').text
    #薪资
    job_salary=job_card.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue').text
    #公司
    #如果最后一项没有显示在屏幕上，可以加一个判断
    company='默认公司名'
    ele=job_card.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    #如果找到目标元素-公司名
    if ele !=[]:
        company=ele[0].text

    print(f'职位：{job_name} 薪资{job_salary}：公司{company}')


driver.quit()

