# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 服务.py
# @ide: PyCharm
# @time: 2020/7/4 19:36
import socket


# 创建socket对象
from python进阶.day4.文件上传.fileLib import post_file

sk = socket.socket()
# 绑定ip地址和端口号
sk.bind(("127.0.0.1", 13003))
# 监听
sk.listen()
# 等待传入连接
conn, addr = sk.accept()

post_file(conn, r"D:\learn-automated-testing\code\python进阶\day4\文件上传\服务端\\aa.jpg")
conn.close()
sk.close()
