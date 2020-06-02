
from selenium import webdriver

from seleniumStu.day6.mySettings import driverPath,DOMAIN


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

        return cls._driver



