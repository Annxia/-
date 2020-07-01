# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 4.装饰器.py
# @ide: PyCharm
# @time: 2020/6/30 15:41



def bar(f):
    """
    函数接受一个参数
    函数里边定义一个内部函数
    将定义的内部函数作为返回值返回
    :param f:接受的参数就是被装饰函数，也就是需要增加新功能的函数
    :return:装饰完成后的函数
    """
    def inner():
        f() # 需要保留被装饰函数原有的功能，所以通过参数传递的方式调用被装饰函数
        print("加上了新功能")

    return inner

@bar  #这个操作就相当于 foo = bar(foo)
def foo():
    print("成功实现了一系列功能")


# foo = bar(foo) # 将inner赋值给foo
foo() # 调用foo,就相当于调用inner