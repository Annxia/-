# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 7.死锁.py
# @ide: PyCharm
# @time: 2020/7/1 22:17
import threading
import time

# 同步锁
lockA = threading.Lock()  #面试官的锁
lockB = threading.Lock()  #小明的锁

# 面试官
def foo1():
    lockA.acquire()
    print("提问")
    time.sleep(1)

    lockB.acquire()
    print("发offer")
    time.sleep(1)

    lockA.release()
    lockB.release()

# 小明
def foo2():
    lockB.acquire()
    print("请给我offer")
    time.sleep(1)

    lockA.acquire()
    print("回答")
    time.sleep(1)

    lockB.release()
    lockA.release()

t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)
t1.start()
t2.start()

# 以上代码的核心：由于是多线程，所以两个函数交替执行，线程一的锁A上锁
# 然后切换到线程二，线程二此刻也操作了A上锁

