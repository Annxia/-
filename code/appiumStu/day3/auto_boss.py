from appium import webdriver

from config import *

# 初始化webdriver
def setup():
    driver = webdriver.Remote('http://localhost:4723/wd/hub',boss_caps)
    driver.implicitly_wait(10)
    return driver

# 清除
def teardown(driver):
    driver.quit()


def search_job(driver):
    # 点击放大镜
    eles = driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')  # 先取所有符合条件的元素
    # 找到第二个元素--放大镜
    btn = eles[1]
    btn.click()

    # 搜索框输入职位信息
    search_input = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
    search_input.send_keys('软件测试')  # 输入参数

    # 选择符合条件的第一个搜索结果
    driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()

    # 获取当前页面所有职位信息元素
    job_msg = driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

    for job in job_msg:
        # 输出岗位名称
        name = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
        # print(name.text)
        # 输出薪资
        salray = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
        # print(salray.text)
        # 输出公司名称
        company = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_company_name')

        # print('%s|%s|%s' % (name.text, salray.text, company.text))


# 查看第一个结果里面的岗位信息
def detail_job(driver):
    # 点击第一个岗位
    driver.find_element_by_id('com.hpbr.bosszhipin:id/view_job_card').click()
    # 搜集岗位信息:地点-年限-学历
    location = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_location').text
    exp = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_work_exp').text
    degree = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_degree').text
    print(f'地区:{location},年限:{exp},学历{degree}')


if __name__ == '__main__':
    driver = setup()
    search_job(driver)
    detail_job(driver)
    teardown(driver)