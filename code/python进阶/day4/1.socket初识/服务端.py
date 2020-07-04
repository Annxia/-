# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 服务端.py
# @ide: PyCharm
# @time: 2020/7/4 18:31
import socket

#创建 socket 对象
sk = socket.socket()
# 绑定一个 ip 地址和端口号
sk.bind(("127.0.0.1", 13000))

# 监听，有没有请求过来
sk.listen()

print("服务端启动了...")

# 阻塞状态：等待传入连接
# 连接成功之后会返回一个新的套接字对象和客户端的ip地址
conn, addr = sk.accept()
print("客户端ip地址:", addr)

# 接收消息
client_data = conn.recv(1024).decode("utf8")
print("客户端：", client_data)

inp = input(">>>")
# 发送数据
conn.sendall(inp.encode("utf8"))

# 释放资源
conn.close()
sk.close()