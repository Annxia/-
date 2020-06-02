from selenium.webdriver.common.by import By

from seleniumStu.day6.抽离出basePage的版本.basePage import basePage


class LoginPage(basePage):
    '''登录页面'''
    def __init__(self):
        # 执行父类的构造方法

        super().__init__()
        # 访问网址
        # self.driver.get("http://127.0.0.1:8088/login")

        # 用户名输入框，密码输入框，登录按钮的定位方法和表达式
        self.userInploc = (By.NAME, "username")
        self.pwdInploc = (By.NAME, "password")
        self.loginBtnloc = (By.TAG_NAME, "button")

    def userInpBox(self):
        "实时获取用户名输入框"
        return self.get_element(self.userInploc)

    def pwdInpBox(self):
        return self.get_element(self.pwdInploc)

    def loginBtnBox(self):
        return self.get_element(self.loginBtnloc)


# 抽离出页面动作类，继承页面类,把常用的公共方法封装起来
class LoginPageAction(LoginPage):
    def login(self):
        # # 输入用户名
        # self.userInpBox().send_keys("libai")
        # # 输入密码
        # self.pwdInpBox().send_keys("opmsopms123")
        # # 点击登录按钮
        # self.loginBtnBox().click()

        input("输入任意字符继续运行>>>")
        self.driver.quit()


if __name__ == '__main__':
    loginPageActionObj = LoginPageAction()
    loginPageActionObj.login()
