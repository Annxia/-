# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: testlib2.py
# @ide: PyCharm
# @time: 2020/7/11 20:15

import requests
# 定义一个函数获取教管系统当前课程
def get_course():
    resp = requests.get('')
    return resp.json()