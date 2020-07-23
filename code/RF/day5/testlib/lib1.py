# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: lib1.py
# @ide: PyCharm
# @time: 2020/7/23 22:38

def returnlist():
    return [1,2]

#如果该函数设计为RF关键字，则不可以有下滑线作为前置
#一般一个下滑线会默认为私有函数或方法，不会被RF引用为关键字
def _returnlist2():
    return [1,2]


#中间带下滑线的被RF引用时可以省略或用空格代替下滑线
def return_list3():
    return [1,2]