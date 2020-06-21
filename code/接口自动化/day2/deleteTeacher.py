import requests

from 接口自动化.day2.login import login

Host = 'http://127.0.0.1:80'
api_url = f'{Host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
user_cookie = login('auto','sdfsdfsdf')

payload = {
    'action':'delete_teacher',
    'id':260
}

reps = requests.delete(api_url,data=payload,cookies=user_cookie)
reps.encoding = 'unicode_escape'
print(reps.text)