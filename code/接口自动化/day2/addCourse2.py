import json

import requests
from 接口自动化.day2.login import login

Host = 'http://127.0.0.1:80'
api_url = f'{Host}/apijson/mgr/sq_mgr/'
header = {'Content-Type':'application/json'}
user_cookie = login('auto','sdfsdfsdf')

payload = {
    "action":"add_course_json",
    "data": '''{
        "name":"初中化学",
        "desc":"初中化学课程",
        "display_idx":"4"
    }'''
}

reps = requests.post(api_url, json=payload, headers=header, cookies=user_cookie)
reps.encoding = 'unicode_escape'
print(reps.text)