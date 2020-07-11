# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: course_mgr.py.py
# @ide: PyCharm
# @time: 2020/7/11 21:04

'''
创建一个测试套件文件，实现 2个测试用例：
用例1：

    1.  用Python语言开发一个测试库 course_mgr.py。
        该库有一个函数 listCourse 可以返回教管系统的所有课程（可以使用requests库开发）。


    2.  用RF测试用例来使用 listCourse 关键字， 根据其返回的课程列表，
        将所有的课程名输出到日志文件中（使用循环）
        验证是否和预期课程相同

用例2：
    登录网站https://www.vmall.com/index.html
    获得所有热销单品的名称，打印在log报表中

'''
import requests

HOST = "http://127.0.0.1:80"

def login(username, password):
    login_url = f'{HOST}/api/mgr/loginReq'
    payload = {'username':username,'password':password}
    reps = requests.post(login_url,data=payload)
    reps.encoding = 'unicode_escape'# 设置响应编码--显示中文
    return reps.cookies


def list_course():
    apiUrl = f'{HOST}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
    user_cookie = login('auto', 'sdfsdfsdf')

    resp = requests.get(apiUrl, cookies=user_cookie)
    course_list =  resp.json()['retlist']
    return [one['name'] for one in course_list]

if __name__ == '__main__':
    print(list_course())