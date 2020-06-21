import requests

from 接口自动化.day2.login import login

Host = 'http://127.0.0.1:80'
api_url = f'{Host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
user_cookie = login('auto','sdfsdfsdf')

payload = {
    'action':'modify_teacher',
    'id':261,
    'newdata':'''{
        "username":"lishiming",
        "password":"sq888",
        "realname":"李世民",
        "desc":"李世民老师",
        "courses":[{"id": 2164, "name": "大学英语158973996695"}],
        "display_idx":1
    }'''
}

reps = requests.put(api_url,data=payload,cookies=user_cookie)
reps.encoding = 'unicode_escape'
print(reps.text)