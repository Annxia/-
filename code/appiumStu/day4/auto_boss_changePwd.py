#导包
import time

from appium import webdriver


class BossZP():
    def __init__(self):
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
            # 'skipServerInstallation':True,
        }
        #初始化webdriver
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
        self.driver.implicitly_wait(10)


    def get_pwd(self):
        self.new_password=input('请输入原密码：')
        self.old_password=input('请输入新密码：')

    def change_password(self,old_password,new_password):
        # 1.进入我的标签
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()

        # 2.点击右上角设置图标
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
        # 3.进入账号与绑定
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()
        time.sleep(1)
        # 4.进入设置密码
        self.driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/*[2]/android.view.ViewGroup').click()

        # 5.完成密码设置
        #5.1输入旧密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(old_password)
        #5.2输入新密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(new_password)
        #5.3输入确认密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(new_password)
        #5.4点击修改密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()


    def login(self,password):
        #选择账号密码登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()

        #使用新密码登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(password)
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()

        #校验是否登录成功
        xpath='//*[@resource-id="com.hpbr.bosszhipin:id/title_container"]//android.widget.TextView'
        title=self.driver.find_element_by_xpath(xpath).text
        print(title)
        assert title=='测试工程师'

    #退出
    #quit这个函数可不可以做的简单一点
    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    boss=BossZP()
    boss.get_pwd()
    boss.change_password(boss.old_password,boss.new_password)
    boss.login(boss.new_password)
