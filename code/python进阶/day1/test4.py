# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : test4.py
# @ide     : PyCharm
# @time    : 2020/6/28 21:35

data = ""

with open("./qqjt.png", "rb") as f:
    data = f.read()

with open("./qqjt1.png", "wb") as f:
    f.write(data)
