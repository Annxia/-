import requests

Host = "http://127.0.0.1:80"
apiUrl = f'{Host}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'

reps = requests.get(apiUrl)
reps.encoding = 'unicode_escape'# 设置响应编码--显示中文
print(reps.text)# 打印响应内容--字符串类型