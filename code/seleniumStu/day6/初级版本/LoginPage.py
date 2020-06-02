from seleniumStu.day6.初级版本.myDriver import Driver


class LoginPage:
    '''登录页面'''
    def __init__(self):
        # 创建driver对象
        self.driver = Driver.get_driver()
        # 访问网址
        self.driver.get("http://127.0.0.1:8088/login")

        # 用户名输入框
        # self.userInp = self.driver.find_element_by_name("username")
        # 密码输入框
        # self.pwdInp = self.driver.find_element_by_name("password")
        # 登录按钮
        # self.loginBtn = self.driver.find_element_by_css_selector("button")

    #     # 用户名输入框的定位方法和表达式
    #     self.userInplocat = (By.NAME,"username")
    #     self.pwdInplocat = (By.NAME,"password")
    #     self.loginBtnlocat = (By.CSS_SELECTOR,"button")
    #
    # def userInpBox(self):
    #     return self.driver.find_element(self.userInplocat[0],self.userInplocat[1])
    def userInpBox(self):
        "实时获取用户名输入框"
        return self.driver.find_element_by_name("username")

    def pwdInpBox(self):
        return self.driver.find_element_by_name("password")

    def loginBtnBox(self):
        return self.driver.find_element_by_css_selector("button")


# 抽离出页面动作类，继承页面类,把常用的公共方法封装起来
class LoginPageAction(LoginPage):
    def login(self):
        self.userInpBox().send_keys("libai")
        self.pwdInpBox().send_keys("opmsopms123")
        self.loginBtnBox().click()


if __name__ == '__main__':
    loginPageActionObj = LoginPageAction()
    loginPageActionObj.login()
