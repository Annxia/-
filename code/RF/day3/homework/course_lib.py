# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: course_lib.py
# @ide: PyCharm
# @time: 2020/7/22 22:30
import time

from selenium import webdriver


def deleteAllLesson():
    driver = webdriver.Chrome()
    #隐式等待----只有在找不到元素时才会触发
    driver.implicitly_wait(2)
    driver.get("http://localhost/mgr/login/login.html")
    #开始登录
    # driver.find_element_by_id("username").send_keys('auto')
    # driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn-success').click()

    # 删除所有课程
    while 1:
        del_btns = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if del_btns == []:
            print("课程删除完毕，退出循环")
            break

        # 点击删除按钮
        del_btns[0].click()
        # 点击确认框
        driver.find_element_by_css_selector('.btn-primary').click()
        # 等待弹出框消失
        time.sleep(1)

    driver.quit()

if __name__ == '__main__':
    deleteAllLesson()