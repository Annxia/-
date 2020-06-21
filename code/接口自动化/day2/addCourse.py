import requests

# 路径url
from 接口自动化.day2.login import login

user_cookie = login('auto','sdfsdfsdf')
Host = "http://127.0.0.1:80"
api_url = f'{Host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
# 参数
payload = {
        'action': 'add_course',
        'data': """{
          "name":"初中化学",
          "desc":"初中化学课程",
          "display_idx":"4"
        }"""
    }
reps = requests.post(api_url,data=payload,cookies=user_cookie)
reps.encoding = 'unicode_escape'# 设置响应编码--显示中文
print(reps.text)# 打印响应内容--字符串类型


# http://121.41.14.39:2001/user/goUpload