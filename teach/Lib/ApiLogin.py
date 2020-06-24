import requests


class Login:
    def api_login(self,username, password):
        HOST = "http://127.0.0.1:80"
        login_url = f'{HOST}/api/mgr/loginReq'
        payload = {'username': username, 'password': password}
        reps = requests.post(login_url, data=payload)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.cookies['sessionid'],reps.text


if __name__ == '__main__':
    s = Login().login('auto','sdfsdfsdf')
    print(s)