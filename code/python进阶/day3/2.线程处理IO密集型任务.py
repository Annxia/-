# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 2.线程处理IO密集型任务.py
# @ide: PyCharm
# @time: 2020/7/1 20:44
import threading
import time


def foo(something):
    print(something)
    time.sleep(2)


begin_time = time.time()
"""
# 总计耗时： 4.001197814941406
foo("发送接口请求")
foo("等待接收接口返回并处理")
"""

# 总计耗时： 0.0020046234130859375
t1 = threading.Thread(target=foo, args=['发送接口请求'])
t2 = threading.Thread(target=foo, args=['等待接收接口返回并处理'])

t1.start()
t2.start()

# 阻塞住主线程,不影响其他子线程
t1.join()
t2.join()

end_time = time.time()
print("总计耗时：",end_time-begin_time)

"""
主线程结束想要退出的时候会去检查子线程的状态
如果发现子线程没有结束，或者子线程仍需要时间运行
那么，主线程就会等待，直到所有子线程结束运行，再退出
（所以end_time此时会自己先结束自己的主线程,要想等待所有子线程结束主线程再结束，需要阻塞一下主线程）
"""
