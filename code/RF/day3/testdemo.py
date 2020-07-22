# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: testdemo.py
# @ide: PyCharm
# @time: 2020/7/19 15:53


from robot.api import logger
def check_score(score):
    if int(score)>60:
        print('恭喜你及格了')
        logger.console("恭喜你及格了")
    else:
        print('不及格，再好好复习')
        logger.console('不及格，再好好复习')