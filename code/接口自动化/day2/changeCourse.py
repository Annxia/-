import requests

from 接口自动化.day2.login import login

Host = "http://127.0.0.1:80"
api_Url = f"{Host}/api/mgr/sq_mgr/"
header = {'Content-Type':'application/x-www-form-urlencoded'}
user_cookie = login('auto','sdfsdfsdf')
payload = {
    'action':'modify_course',
    'id':'2172',
    'newdata':'''{
        "name":"初中化学12354",
        "desc":"初中化学课程12138",
        "display_idx":"138"
    }
    '''
}
reps = requests.put(api_Url,data=payload,cookies=user_cookie)
reps.encoding = 'unicode_escape'
print(reps.text)
