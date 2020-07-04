# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 追求者大白(客户端).py
# @ide: PyCharm
# @time: 2020/7/4 19:10
import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 13001))
print("大白客户端启动了...")

while True:
    inp = input(">>>")
    # 向女神发送数据
    sk.sendall(inp.encode("utf8"))

    if inp == "exit":
        break

    # 接收服务端消息
    client_data = sk.recv(1024).decode("utf8")
    print("女神回复：", client_data)

sk.close()