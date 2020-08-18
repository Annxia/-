import requests


def login(username, password):
    HOST = "http://127.0.0.1:80"
    login_url = f'{HOST}/api/mgr/loginReq'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    payload = {'username':username,'password':password}
    reps = requests.post(login_url,data=payload)
    reps.encoding = 'unicode_escape'# 设置响应编码--显示中文
    # print(reps.text)

    # 1- 查看下cookie
    # print(reps.headers) #响应头
    # print(reps.cookies) #打印cookies对象，jar格式

    # 2-cookie自定义--获取完set-cookie----自己加参数
    # print(reps.cookies['sessionid'])
    # #调用时：自己封装
    # user_session = reps.cookies['sessionid']
    # user_cookie = {'sessionid':user_session}

    return reps.cookies

'''
1.json参数---建议使用
    reps = requests.post(api_url,json=payload)
2.data参数
import json
reps = requests.post(api_url,data=json.dumps(payload),headers = header)
'''

if __name__ == '__main__':
    print(login('auto','sdfsdfsdf'))