# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: homeworkTeacher.py
# @ide: PyCharm
# @time: 2020/6/30 14:59

with open("./gbk编码.txt", "r", encoding="gbk") as f1, open("./utf8编码.txt", "r", encoding="utf8") as f2:
    str = f1.read() + "\n" + f2.read()
    print(str)

filename = input("请输入新的文件名：")
with open(f"./{filename}.txt", "w", encoding="utf8") as f:
    f.write(str)
