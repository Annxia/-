# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 女神苏苏.py
# @ide: PyCharm
# @time: 2020/7/4 19:19
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # 接收数据
            client_data = self.request.recv(1024).decode("utf8") # 相当于conn.recv()
            print("客户端：", client_data)
            if client_data == "exit":
                break
            # 发送数据：
            self.request.sendall(input(">>>").encode("utf8"))

        self.request.close()


server = socketserver.ThreadingTCPServer(("127.0.0.1",13002), MyServer)
print("女神上线了...")
server.serve_forever()
