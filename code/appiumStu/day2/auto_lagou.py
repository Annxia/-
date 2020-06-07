#导包
import traceback

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
    'unicodeKeyboard': True,#如果指定UI2作为驱动，不需要配置
    'resetKeyboard':True,#重置自动化时设置的键盘
}

try:
    #初始化driver对象-用于控制手机
    driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    driver.implicitly_wait(10)#稳定元素


    #点击弹出搜索框
    search_bar=driver.find_element_by_id('com.alpha.lagouapk:id/search_tab_txt')
    print(search_bar.text)
    search_bar.click()

    #搜索框输入职位信息
    search_input=driver.find_element_by_id('com.alpha.lagouapk:id/result_Search')
    search_input.send_keys('软件测试')#输入参数

    #待选结果-选择第一个 com.alpha.lagouapk:id/suggest_ps_adpter
    seres=driver.find_elements_by_id('com.alpha.lagouapk:id/suggest_ps_adpter')
    seres[0].click()

    #搜索查询结果-岗位名，待遇，公司
    jobs=driver.find_elements_by_id('com.alpha.lagouapk:id/position_card_content_layout')
    #通过公司信息元素找到详细信息
    for job in jobs:
        name=job.find_element_by_id('com.alpha.lagouapk:id/position_name').text
        salary=job.find_element_by_id('com.alpha.lagouapk:id/position_card_salary').text
        company=job.find_element_by_id('com.alpha.lagouapk:id/position_card_company_name').text

        print(f'公司：{company}|职位：{name}|待遇：{salary}')


except :
# input('......')
    print(traceback.format_exc())
    pass

finally:
    driver.quit()