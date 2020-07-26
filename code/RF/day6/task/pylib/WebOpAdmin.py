# coding:utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cfg import *
import time

class WebOpAdmin():
    # 保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setupWebTest(self,driverType='chrome'):
        # self.cur_wd 保存 WebDriver 对象
        self.cur_wd = None
        if driverType == 'chrome':
            self.cur_wd =  webdriver.Chrome()
        elif driverType == 'firefox':
            self.cur_wd =  webdriver.Firefox()
        else:
            raise Exception('unknow driver type %s' % driverType)

        self.cur_wd.implicitly_wait(10)


    def tearDownWebTest(self):
        self.cur_wd.quit()


    def DeleteAllCourse(self):

        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)


    def DeleteAllTeacher(self):

        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)


    # delete_xxx 基本差不多，可以考虑抽象为一个通用的,后面delete班，班期 就不用开发关键字函数了
    def DeleteAll(self,objName):
        if objName=='course':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        elif objName=='teacher':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        else :
            raise Exception('keyword DeleteAll get unknow obj Name %s' % objName)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)


    def loginWebSite(self):
        self.cur_wd.get(MgrLoginUrl)

        self.cur_wd.find_element_by_id('username').send_keys(adminuser['name'])
        self.cur_wd.find_element_by_id('password').send_keys(adminuser['pw'])

        self.cur_wd.find_element_by_tag_name('button').click()



    def AddCourse(self, name,desc,idx):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = self.cur_wd.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        self.cur_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)



    def  AddTeacher(self,realname,username,desc,idx,lesson):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = self.cur_wd.find_element_by_css_selector(
            "textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector(
            'select[ng-model*=courseSelected]'))
        select.select_by_visible_text(lesson)

        self.cur_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)




    def  GetTeacherList(self):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        # 试试 //tr/td[2]/span/text()
        eles = self.cur_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]




    def GetCourseList(self):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()

        # 试试 //tr/td[2]/span/text()
        eles = self.cur_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]
