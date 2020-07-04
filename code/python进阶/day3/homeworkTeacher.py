# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: homeworkTeacher.py
# @ide: PyCharm
# @time: 2020/7/4 20:31
import requests
import threading


urls = [
'http://mirrors.163.com/centos/build/rpmcompare5.pl.txt',
'http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt'
]

fileContentList = [None for one in urls]

lock = threading.Lock()


def get_txt(idx, url):
    print("thread #%s start" % idx)
    r = requests.get(url)

    lock.acquire()
    fileContentList[idx] = r.text
    lock.release()

    print("thread #%s end" % idx)


if __name__ == '__main__':
    print("main thread start.")

    threadpool = []

    for idx,url in enumerate(urls):
        print("url类型--------",type(url))
        t = threading.Thread(target=get_txt,args=(idx, url))
        t.start()
        threadpool.append(t)

    for t in threadpool:
        t.join()

    mergeTxt = "\n\n----------------\n\n".join(fileContentList)
    print(mergeTxt)

    with open("./readme88.txt", 'w', encoding="utf8") as f:
        f.write(mergeTxt)

    print("main thread end")




