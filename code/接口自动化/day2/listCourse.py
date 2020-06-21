from pprint import pprint

import requests
from 接口自动化.day2.login import login

Host = "http://127.0.0.1:80"
apiUrl = f'{Host}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
user_cookie = login('auto','sdfsdfsdf')

reps = requests.get(apiUrl,cookies=user_cookie)
reps.encoding = 'unicode_escape'# 设置响应编码--显示中文
pprint(reps.text)# 打印响应内容--字符串类型