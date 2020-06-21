import json
from pprint import pprint

import requests
import hashlib #算法库

# 1----------get_token--获取token---密码需要MD5加密
token_url = 'http://121.41.14.39:2001/token/token'
psw = hashlib.md5(b'zr111111hg').hexdigest() #一定是byte,获取16进制的值hexdigest()
print(psw)
payload = {
    'mobile':'13588000000',
    'password':psw
}
reps_token = requests.post(token_url, data=payload)
user_token = json.loads(reps_token.text)['data']
print(reps_token.text)


# 2---------file_upload--上传文件----
file_url = 'http://121.41.14.39:2001/user/doUpload'
# cookie-- 需要自己封装
user_cookie = {'uploadFile':user_token}
header = {'Content-Type':'multipart/form-data'}
# (文件的名字，文件对象，类型)
fileload = {'file':('logo.png',open(r'D:\松勤学习\22-接口自动化\代码资料\logo.png','rb'),'jpg/png/gif')}
reps_file = requests.post(file_url,files=fileload,cookies=user_cookie)
pprint(reps_file.json())