# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : test3.py
# @ide     : PyCharm
# @time    : 2020/6/28 21:26

with open("./a.txt", "w", encoding="utf8") as f:
    f.write("举头西北浮云")

with open("./a.txt", "r", encoding="utf8") as f:
    print(f.read())


