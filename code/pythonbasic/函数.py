# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 函数.py
# @ide: PyCharm
# @time: 2020/8/13 15:35
print("---")
'''
    变量： 是对象的一个名字，方便使用这个对象
    函数： 一段代码的名字，方便使用这段代码
    
None：说明函数没有返回值；或者return后面没有对象
如果return后面跟着一个对象，接收的是一个值，类型不变
如果return后面跟着多个对象，接收的是一个元组
'''
def login():
    i = 1
    while i < 4:
        num = input('请输入密码')
        if num == '123':
            print('登陆成功')
            return # 结束函数的用法
        i += 1
    print('三次机会已使用完毕，登录失败')


login()