from appium import webdriver
#自动化的配置信息
from config import *

#初始化webdriver
def setup():
    driver=webdriver.Remote('http://localhost:4724/wd/hub',boss_caps)
    driver.implicitly_wait(10)
    return driver

def teardown(driver):
    driver.quit()

#搜索岗位信息-自动化测试
def search_job(driver):
    #点击放大镜
    # driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')[1].click()
    driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/*').click()

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

#查看第一个结果里面的岗位信息
def detail_job(driver):
    #点击第一个岗位
    driver.find_element_by_id('com.hpbr.bosszhipin:id/view_job_card').click()
    #搜集岗位信息-地点-年限-学历
    location= driver.find_element_by_id('tv_required_location').text
    exp=driver.find_element_by_id('tv_required_work_exp').text
    degree=driver.find_element_by_id('tv_required_degree').text
    print(f'地区：{location},工作经验{exp},学历{degree}')


if __name__ == '__main__':
    driver=setup()
    search_job(driver)
    detail_job(driver)
    teardown(driver)



