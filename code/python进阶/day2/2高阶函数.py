# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2高阶函数.py
# @ide     : PyCharm
# @time    : 2020/6/29 21:21
"""
# 函数名可以赋值给其他变量
def foo(name):
    print(name)


bar = foo  # 就是一个变量赋值
print(foo)
print(bar)

bar("张三")
"""
"""
# 函数名作为参数传递
def bar():
    print("我是bar函数")

def foo(f):
    f()

foo(bar())
"""


# 函数名作为返回值
def foo():
    def inner():
        print("我是inner")

    return inner

a = foo()
print(a)
a()
