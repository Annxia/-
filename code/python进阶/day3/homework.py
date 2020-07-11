# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: homework.py
# @ide: PyCharm
# @time: 2020/7/4 21:11
"""
先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。

http://cn.python-requests.org/zh_CN/latest/user/quickstart.html

然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容

http://mirrors.163.com/centos/6/isos/x86_64/README.txt
http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt

主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中
"""
import requests
import threading

urls = [
'http://mirrors.163.com/centos/build/rpmcompare5.pl.txt',
'http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt'
]

fileContentList = []
# 设置一个同步锁，读完一个url再去读下一个
lock = threading.Lock()


def get_txt(url):
    reqs = requests.get(url)
    print("text",reqs.text)
    lock.acquire()
    fileContentList.append(reqs.text)
    lock.release()


t1 = threading.Thread(target=get_txt, args=(urls[0],))
t2 = threading.Thread(target=get_txt, args=(urls[1],))
t1.start()
t1.join()
t2.start()
t2.join()


mergeTxt = "\n\n----------------\n\n".join(fileContentList)
print(mergeTxt)
with open("./readme89.txt", 'w', encoding="utf8") as f:
    f.write(mergeTxt)
