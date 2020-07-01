# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 3.线程处理计算密集型任务.py
# @ide: PyCharm
# @time: 2020/7/1 21:27
import threading
import time


def foo():
    num = 0
    for i in range(1000000):
        num = num + 1

begin_time = time.time()

"""
# 串行，总计耗时：2.0012106895446777 
foo()
foo()
"""
# 并行,总计耗时：2.0020854473114014
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)

t1.start()
t2.start()

# 阻塞住主线程,不影响其他子线程
t1.join()
t2.join()

end_time = time.time()
print("总计耗时：", end_time-begin_time)
