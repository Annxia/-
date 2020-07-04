# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: fileLib.py
# @ide: PyCharm
# @time: 2020/7/4 19:37
import os


def post_file(sk_obj, file_path):
    """
    发送文件
    :param sk_obj: socket对象
    :param file_path: 文件路径
    :return:
    """
    # 发送文件大小
    file_size = os.stat(file_path).st_size
    sk_obj.sendall(str(file_size).encode("utf8"))
    sk_obj.recv(1024)

    # 发送文件名称
    sk_obj.sendall(os.path.split(file_path)[1].encode("utf8"))
    sk_obj.recv(1024)

    # 发送文件内容
    with open(file_path, 'rb') as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size -= 1024


def get_file(sk_obj):
    """
    接收文件
    :param sk_obj: socket对象
    :return:
    """
    # 接收文件大小
    file_size = int(sk_obj.recv(1024).decode("utf8"))
    sk_obj.sendall(b"ok")

    #接收文件名称
    file_name = sk_obj.recv(1024).decode("utf8")
    sk_obj.sendall(b"ok")

    # 接收文件内容
    with open("./a.jpg", "wb") as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size -= 1024