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
    'skipServerInstallation':True
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#点击放大镜
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/.').click()


#搜索框输入职位信息
search_input=driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')#输入参数

#选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()


#获取当前页面所有职位信息元素
job_msg=driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

for job in job_msg:
    #输出岗位名称
    name=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
    # print(name.text)
    #输出薪资
    salray=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
    # print(salray.text)
    #输出公司名称
    #找到元素返回包含一个元素的列表，找不到就返回空列表
    company=job.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    #避免屏幕遮挡了公司名，查到不到目标元素，设置一共默认值
    company_text = '空'
    #当找打company元素的时候，就使用该元素的文本
    if company:
        company_text=company[0].text

    print('%s|%s|%s'%(name.text,salray.text,company_text))



#点击第一个搜索结果
job_msg[0].click()

#获取职位名称下面的信息：地区、工作年限、学历、工作性质
location=driver.find_element_by_id('tv_required_location').text

work_exp=driver.find_element_by_id('tv_required_work_exp').text

degree=driver.find_element_by_id('tv_required_degree').text

print(f'地区：{location}|工作经验：{work_exp}|学历:{degree}')



driver.quit()