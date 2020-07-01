# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 8.可重入锁.py
# @ide: PyCharm
# @time: 2020/7/1 22:28
import threading
import time


# 递归锁
lockR = threading.RLock()
"""
递归锁内部维护着一把锁和一个计数器
每次上锁，计数器+1
每次解锁，计数器-1
计数器可以 >= 0,但不能 < 0
"""
# 面试官
def foo1():
    lockR.acquire()
    print("提问")
    time.sleep(1)

    lockR.acquire()
    print("发offer")
    time.sleep(1)

    lockR.release()
    lockR.release()


# 小明
def foo2():
    lockR.acquire()
    print("请给我offer")
    time.sleep(1)

    lockR.acquire()
    print("回答")
    time.sleep(1)

    lockR.release()
    lockR.release()


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)
t1.start()
t2.start()