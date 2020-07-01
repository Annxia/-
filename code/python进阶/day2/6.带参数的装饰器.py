# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 6.带参数的装饰器.py
# @ide: PyCharm
# @time: 2020/6/30 20:35


# 这个bar函数就是装饰器
def wraper(age):
    def bar(f):
        """
        函数接受一个参数
        函数里边定义一个内部函数
        将定义的内部函数作为返回值返回
        :param f:接受的参数就是被装饰函数，也就是需要增加新功能的函数
        :return:装饰完成后的函数
        """

        def inner(name):
            print("年龄", age)
            f(name)  # 需要保留被装饰函数原有的功能，所以通过参数传递的方式调用被装饰函数
            print("利用摄像头，捕捉用户视网膜成像，然后分析，得到手机壳颜色，再修改ui主题颜色")

        return inner
    return bar

@wraper(18)  # 第一层， foo == bar() # 第二层 foo == inner
def foo(name):
    print("测试订单", name)


foo("张三")
