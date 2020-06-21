from pprint import pprint

import requests

from 接口自动化.day2.login import login

Host = "http://127.0.0.1:80"
api_url = f'{Host}/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20'
header = {'Content-Type':'application/x-www-form-urlencoded'}
user_cookie = login('auto','sdfsdfsdf')

reps = requests.get(api_url,cookies=user_cookie)
reps.encoding = 'unicode_escape'
pprint(reps.text)