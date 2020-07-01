# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : test5.py
# @ide     : PyCharm
# @time    : 2020/6/28 21:44

import chardet


# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, "rb") as f:
        data = f.read()
        return chardet.detect(data)

file_path = "./c.txt"
eData = get_encoding(file_path)
print(eData)
