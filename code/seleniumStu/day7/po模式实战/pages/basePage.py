from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumStu.day7.po模式实战.utils.myDriver import Driver
from seleniumStu.day7.po模式实战.utils.mySettings import TIMEOUT,POLL_FREQUENCY,DOMAIN


class BasePage:
    def __init__(self):
        """
        所有页面的基类，封装所有页面的
        """
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver()

        # 域名
        self.url = DOMAIN

    def get_element(self,locator):
        """
        根据表达式匹配元素对象
        :param locator:
        :return:
        """
        # 判断元素是否存在
        WebDriverWait(
            # 传入浏览器驱动对象
            driver = self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUENCY).until(
            # 检测元素是否可见
            EC.visibility_of_element_located(locator)
        )
        # 返回元素对象
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """
        根据表达式匹配元素列表
        :param locator:
        :return:
        """
        # 判断元素是否存在
        WebDriverWait(
            # 传入浏览器驱动对象
            driver = self.driver,
            # 传入超时时间
            timeout = 10,
            # 设置轮询时间
            poll_frequency=0.5).until(
            # 检测元素是否可见
            EC.visibility_of_element_located(locator)
        )
        # 返回元素列表
        return self.driver.find_elements(*locator)

