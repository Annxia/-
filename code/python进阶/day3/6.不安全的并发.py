# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 6.不安全的并发.py
# @ide: PyCharm
# @time: 2020/7/1 21:58
import threading
import time

balance = 500 #银行卡账户余额
r = threading.Lock() # 声明是一把锁
"""
这把锁是同步锁
同步锁必须"上锁和解锁"相对应

如果上锁之后，不解锁，再次上锁,代码会阻塞
如果解锁之后，没有锁的时候，又进行解锁，代码会报错
"""
# 操作账户余额
def foo(num):
    # 申明全局变量
    global balance
    r.acquire()


    # 将变量存到自己的系统
    account_balance = balance
    time.sleep(1) #防止代码太少，CPU执行速度太快，t1和t2变成串行

    # 省略其他业务处理逻辑时，直接计算余额
    account_balance = account_balance + num
    # 将计算结果传递回去
    balance = account_balance

    r.release()


# 消费300元
t1 = threading.Thread(target=foo, args=[-300])
# 收入 10000 元
t2 = threading.Thread(target=foo, args=[10000])
t1.start()
t2.start()
t1.join()
t2.join()

print("最终余额：", balance)