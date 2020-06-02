
from selenium import webdriver

from seleniumStu.day6.homework.mySettings import driverPath,DOMAIN


class Driver:
    # 浏览器驱动对象初始化为空
    _driver = None

    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        '''
        获取浏览器对象
        :param browser_name:浏览器类型，比如Chrome,FireFox
        :return: 浏览器驱动对象
        '''

        # 如果不为空就不需要创建了
        if cls._driver is None:
            if browser_name == "Chrome":
                cls._driver = webdriver.Chrome(driverPath['Chrome'])
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
        # 登录逻辑
        cookieSli =[
            {'domain': '127.0.0.1',
             'httpOnly': False,
             'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
             'path': '/',
             'secure': False,
             'value': '1590652021'},
            {'domain': '127.0.0.1',
             # 'expiry': 1622188021,
             'httpOnly': False,
             'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
             'path': '/',
             'secure': False,
             'value': '1590652008'},
            {'domain': '127.0.0.1',
             # 'expiry': 1622188007.526022,
             'httpOnly': True,
             'name': 'beegosessionID',
             'path': '/',
             'secure': False,
             'value': 'd65a82b5ff3c39c55ba8ca76f7f9f8c1'}

        ]

        # 先清空cookie
        cls._driver.delete_all_cookies()

        for cook in cookieSli:
            cls._driver.add_cookie(cook)
        cls._driver.refresh()


