from config import *

from appium import webdriver

driver = webdriver.Remote('http://localhost:4723/wd/hub',boss_caps)
driver.implicitly_wait(10)

old_password = input("请输入原密码：")
new_password = input("请输入新密码：")

def changePassword():
    # 修改密码：点击我的
    driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()

    # 点击设置
    driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()

    # 点击账号与绑定
    driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()

    # 点击修改密码
    driver.find_element_by_xpath('//*[@text="修改密码"]').click()

    # 输入旧密码
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(old_password)

    # 新密码
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(new_password)

    # 确认密码
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(new_password)

    # 点击按钮"修改密码"
    driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()

    input('进入登录界面(输入任意符号继续):')


def login():
    # 点击账号密码登录
    driver.find_element_by_xpath('//*[@text="账户密码登录"]').click()
    # 输入密码
    driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys(new_password)
    # 点击登录按钮
    driver.find_element_by_xpath('//*[@text="登录"]').click()
    # 校验是否登录成功
    xpath = '//*[@resource-id="com.hpbr.bosszhipin:id/title_container"]//android.widget.TextView'
    title = driver.find_element_by_xpath(xpath).text
    print(title)
    assert title == '测试工程师'


if __name__ == '__main__':
    changePassword()
    login()
    input('登录成功(输入任意符号继续):')
    driver.quit()