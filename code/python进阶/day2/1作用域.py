# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1作用域.py
# @ide     : PyCharm
# @time    : 2020/6/29 20:50

g = 99  # 全局变量


def foo():
    x = 1 # 局部变量
    print(x)
    print(g)

    e = "海客谈瀛洲"  # 嵌套
    def bar():
        l = "nathaniel" # 局部变量
        print(l)
        print(e)
    bar()
    print(e)


# print(x)

foo()
