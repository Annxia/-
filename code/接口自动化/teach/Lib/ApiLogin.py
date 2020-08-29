import json
import requests
from config import HOST


class LoginClass:
    def api_login(self, inData, getSession=True):
        login_url = f'{HOST}/api/mgr/loginReq'
        payload = json.loads(inData)
        reps = requests.post(login_url, data=payload)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        if getSession:
            return reps.cookies['sessionid']
        else:
            return reps.text

if __name__ == '__main__':
    s = LoginClass().api_login('auto','sdfsdfsdf')
    print(s)