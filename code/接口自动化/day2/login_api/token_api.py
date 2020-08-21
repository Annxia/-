# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: token_api.py
# @ide: PyCharm
# @time: 2020/8/19 11:37

#1- 获取token
import json

import requests
def get_token():
    token_url = 'http://47.96.181.17:9090/rest/toController'
    payload = {"userName":"J201903070064","password":"362387359"}
    header = {'Content-Type':'application/json'}
    resp_token = requests.post(token_url,json=payload)
    # print(resp_token.text)
    #先转换成字典--通过键值取值
    token = json.loads(resp_token.text)['token']
    return token

# 2- add_user
def add_user():
    addUser_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
    payload={
        "aac003": "张三",
        "aac004": "1",
        "aac011": "21",
        "aac030": "13575726577",
        "aac01u": "88002255",
        "crm003": "1",
        "crm004": "1",
        "crm00a": "2018-11-11",
        "crm00b": "aaaaaa",
        "crm00c": "2019-02-28",
        "crm00d": "bbbbbb"
    }
    header={'X-AUTH-TOKEN':get_token(),'Content-Type':'application/json'}
    resp_addUser = requests.post(addUser_url, headers= header,json=payload)
    print(resp_addUser.text)

if __name__ == '__main__':
    print(get_token())
    print(add_user())