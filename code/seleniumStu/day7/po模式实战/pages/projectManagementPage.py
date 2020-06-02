"""
项目管理页面
"""
from seleniumStu.day7.po模式实战.pages.basePage import BasePage


class ProjectManagementPage(BasePage):
    def __init__(self, path="project/manage"):
        """
        考勤管理页面类
        """
        super().__init__()
        self.path = self.url + path

    def to_page(self):
        """
        访问此页面的网址
        :param path:
        :return:
        """
        self.driver.get(self.path)