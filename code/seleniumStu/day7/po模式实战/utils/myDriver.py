from selenium import webdriver

from seleniumStu.day7.po模式实战.utils.mySettings import driverPath, DOMAIN, cookieSli


class Driver:
    # 初始化为 None
    _driver = None

    @classmethod
    def get_driver(cls,browser_name="Chrome"):
        """
        如果 浏览器驱动对象不存在，则创建浏览器驱动对象，并将其作为返回值返回
        如果 浏览器驱动对象存在，直接将其作为返回值返回
        :param browser_name:希望创建的浏览器类型
        :return:
        """
        if cls._driver is None:
            # 浏览器驱动对象不存在，创建一个
            if browser_name == "Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == "FireFox":
                cls._driver = webdriver.Firefox(driverPath['FireFox'])

            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认的网址
            cls._driver.get(DOMAIN)
            # 执行登录
            cls.__login()

        return cls._driver

    @classmethod
    def __login(cls):
        """
        私有方法，只能在类的内部使用
        类外部无法使用，子类不能继承
        解决登录问题，只希望在浏览器驱动对象被创建时执行一次登录，以后不需要登录
        :return:
        """

        # 清除所有cookie
        cls._driver.delete_all_cookies()

        for cookie in cookieSli:
            # 添加cookie
            cls._driver.add_cookie(cookie)

        # 刷新一下
        cls._driver.refresh()