# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 客户端.py
# @ide: PyCharm
# @time: 2020/7/4 19:54
import socket

from python进阶.day4.文件上传.fileLib import get_file

sk = socket.socket()
sk.connect(("127.0.0.1", 13003))

get_file(sk)

sk.close()