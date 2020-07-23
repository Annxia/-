# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: lib2.py
# @ide: PyCharm
# @time: 2020/7/23 22:46

from selenium import webdriver
class testlib():
    def getlist(self):
        return [1, 2]

    def _getlist2(self):
        return [1, 2]


class lib2:
    def open_browser(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

from robot.api import logger
class lib3():
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def connect_db(self):
        logger.console(f'正在连接数据库，地址：{self.host}:{self.port}')
