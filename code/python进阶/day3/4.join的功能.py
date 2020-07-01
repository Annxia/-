# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 4.join的功能.py
# @ide: PyCharm
# @time: 2020/7/1 21:36
import threading
import time


def foo():
    time.sleep(3)
    print("test")


t1 = threading.Thread(target=foo)
t1.start()
t1.join() # 在线程t1 结束运行之前,阻塞住主线程，不让继续往下运行

print("主线程最后一行代码")