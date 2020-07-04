# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 女神阿肆(服务端).py
# @ide: PyCharm
# @time: 2020/7/4 19:03
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 13001))
sk.listen()
print("女神上线了，并发了一条朋友圈...")

while True:
    """
    第一层循环：目的是可以接收很多个客户端的请求
    """
    print("女神空闲了...")
    conn, addr = sk.accept()
    print("有人来找女神聊天，是：", addr)

    while True:
        """"
        第二层循环：目的是和单独一个客户端不间断聊天
        """
        # 接收客户端来的消息
        client_data = conn.recv(1024).decode("utf8")
        print("他说：", client_data)

        # 如果收到退出请求，结束当前聊天
        if client_data == "exit":
            break

        # 回复消息
        conn.sendall(input(">>>").encode("utf8"))

    conn.close()