import time

from config import  *

from appium import webdriver

class BOSS_ZP():
    #初始化webdriver
    def __init__(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',boss_caps)
        self.driver.implicitly_wait(10)

    def change_pw(self,old_pw,new_pw):
        #修改密码-点击我的
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()

        #点击设置
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()

        #点击账号与绑定
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()

        #点击修改密码
        self.driver.find_element_by_xpath('//*[@text="修改密码"]').click()

        #修改密码
        #1.输入旧密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(old_pw)
        #2.输入新密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(new_pw)
        #3.确认密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(new_pw)
        #点击修改密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()

    #使用新密码登录
    def login(self,new_pw):
        #点击账号密码登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()
        #输入新密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(new_pw)
        #点击登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()
        #检查登录成功-通过判断底部标签栏文本
        ele=self.driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_tab_4')
        if ele.text=='我的':
            print('成功登录')

    #获取代码
    def get_password(self):
        self.old_pw=input('请输入旧密码')
        self.new_pw=input('请输入新密码')


    #结束收尾--当对象被销毁时，就运行该方法
    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    boss=BOSS_ZP()
    boss.get_password()
    boss.change_pw(boss.old_pw,boss.new_pw)
    boss.login(boss.new_pw)