# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 5.守护线程.py
# @ide: PyCharm
# @time: 2020/7/1 21:38
import threading
import time


a = []


def foo():
    while True:
        a.append("1")
        print("生产了一个包子")
        time.sleep(1)


t1 = threading.Thread(target=foo)
# 设置守护线程，必须在 start 之前
# 其作用就是在主线程结束想要退出的时候，不需要等待子线程运行结束，直接退出
# 只对设置了守护线程的线程生效

t1.setDaemon(True)
t1.start()

for i in range(10):
    if a:
        a.remove("1")
        print("吃掉了一个包子")
    time.sleep(1)

print("不需要再吃包子了")