# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: homework.py
# @ide: PyCharm
# @time: 2020/7/4 21:11
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
t1.start()
t2 = threading.Thread(target=get_txt, args=(urls[1],))
t2.start()


mergeTxt = "\n\n----------------\n\n".join(fileContentList)
print(mergeTxt)
with open("./readme89.txt", 'w', encoding="utf8") as f:
    f.write(mergeTxt)
