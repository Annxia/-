# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 3.闭包.py
# @ide: PyCharm
# @time: 2020/6/30 15:38
def foo():
    x = 10

    def inner():
        """
        在一个内部函数里边，对外部作用域的(但不是全局作用域）变量进行引用，
        那么这个内部函数就被认为是闭包
        :return:
        """
        print(x)
        print("我是inner")

    return inner

a = foo()
a()