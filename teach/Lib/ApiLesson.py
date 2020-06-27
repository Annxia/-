import json
import requests
from config import HOST

class LessonClass:
    # 1- 新增课程
    def add_lesson(self,session,inData):
        user_cookie = {'sessionid':session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 参数
        payload = {
             'action': 'add_course',
             'data': json.dumps(inData) # 转json
        }
        reps = requests.post(api_url, data=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text  # 打印响应内容--字符串类型

    # 2- 列出课程
    def list_lesson(self,session,inData):
        user_cookie = {'sessionid':session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        payload = inData
        reps = requests.get(api_url, params=payload, cookies=user_cookie)

        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text  # 打印响应内容--字符串类型

    # 3- 删除课程
    def delete_lesson(self, session, inId):
        user_cookie = {'sessionid': session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        payload = {'action':'delete_course',
                   'id':int(inId)}
        reps = requests.delete(api_url, data=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text  # 打印响应内容--字符串类型

    # 4- 修改课程
    def modify_lesson(self, session, inId, inData):
        api_Url = f"{HOST}/api/mgr/sq_mgr/"
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        user_cookie = {'sessionid': session}
        payload = {
            'action': 'modify_course',
            'id': int(inId),
            'newdata': inData
        }
        reps = requests.put(api_Url, data=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        print(reps.text)

