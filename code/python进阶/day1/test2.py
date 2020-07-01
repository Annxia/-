# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : test2.py
# @ide     : PyCharm
# @time    : 2020/6/28 21:13


a = "abc"  # 字符串类型
b = b"abc"  # bytes 类型
#
# print(type(a))
# print(type(b))

a1 = "会当凌绝顶，一览众山小"
# str 转为 bytes
b1 = a1.encode("utf8")
print(b1)
# bytes 转为 str
c1 = b'\xe4\xbc\x9a\xe5\xbd\x93\xe5\x87\x8c\xe7\xbb\x9d\xe9\xa1\xb6\xef\xbc\x8c\xe4\xb8\x80\xe8\xa7\x88\xe4\xbc\x97\xe5\xb1\xb1\xe5\xb0\x8f'
print(c1.decode("utf8"))
