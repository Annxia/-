import json
import requests

Host = 'http://127.0.0.1:80'
class Lesson:
    # 1- 新增课程
    def addLesson(self,sessionid,inData):
        user_cookie = {'sessionid':sessionid}
        api_url = f'{Host}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 参数
        payload = {
             'action': 'add_course',
             'data': json.dumps(inData)
        }
        reps = requests.post(api_url, data=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text  # 打印响应内容--字符串类型

    # 2- 列出课程
    def listLesson(self):
        pass

    # 3- 删除课程
    def deleteLesson(self):
        pass

    # 4- 修改课程
    def modifyLesson(self):
        pass

