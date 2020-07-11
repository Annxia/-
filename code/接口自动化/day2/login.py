import requests


def login(username, password):
    HOST = "http://127.0.0.1:80"
    login_url = f'{HOST}/api/mgr/loginReq'
    payload = {'username':username,'password':password}
    reps = requests.post(login_url,data=payload)
    reps.encoding = 'unicode_escape'# 设置响应编码--显示中文
    # print(reps.text)

    # print(reps.headers) #响应头
    # print(reps.cookies) #打印cookies对象，jar格式

    return reps.cookies


if __name__ == '__main__':
    print(login('auto','sdfsdfsdf'))