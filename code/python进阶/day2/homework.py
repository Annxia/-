# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: homework.py
# @ide: PyCharm
# @time: 2020/6/30 15:13
import uuid

user_dict = { #存用户名和密码
    "user1": "123",
    "user2": "123"
}
token =""

def login(f):
    def wrapper(*args, **kwargs):
        global token
        if token:
            f(*args,**kwargs)
        else:
            name = input("请输入用户名：").strip()
            password = input("请输入密码：").strip()

            if name in user_dict and user_dict[name] == password:
                f(*args, **kwargs)
                token = str(uuid.uuid4()).replace("-","",-1)
            else:
                print("帐号不存在")
    return wrapper

@login
def my_log():
    print('this is my_log')

@login
def my_name(name):
    print('欢迎登录',name)

@login
def my_shopping_mall():
    print('商城购物')


while True:
    choose_num = input("\n\n1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项(输入q退出)>>>")
    if choose_num =='q' or choose_num =='Q':
        break
    elif choose_num == "1":
        my_log()
    elif choose_num == '2':
        my_name("张三")
    elif choose_num == "3":
        my_shopping_mall()
    else:
        print("输入不合法")
