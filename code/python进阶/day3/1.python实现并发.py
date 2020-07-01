# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 1.python实现并发.py
# @ide: PyCharm
# @time: 2020/7/1 20:13
import threading
import time

def foo(something,num):
    for i in range(num):
        print("cpu 正在：",something)
        time.sleep(1)


# 创建线程：t1,t2
# target指向任务函数，args 为 target 指向的任务函数传参
t1 = threading.Thread(target=foo, args=["一号坑正在深挖", 5])
t2 = threading.Thread(target=foo, args=["二号坑正在深挖", 5])

# 启动线程, 线程之间资源是竞争的
t1.start()
t2.start()
