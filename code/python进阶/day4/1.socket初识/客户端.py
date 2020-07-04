# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 客户端.py
# @ide: PyCharm
# @time: 2020/7/4 18:49
import socket

# 创建socket对象
sk = socket.socket()

# 发起连接
sk.connect(("127.0.0.1", 13000))

inp = input(">>>")
# 发送数据
sk.sendall(inp.encode("utf8"))

# 接收消息
client_data = sk.recv(1024).decode("utf8")
print("服务端：", client_data)
