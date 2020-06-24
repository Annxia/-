import json
from Lib.ApiLogin import Login
from Lib.ApiLesson import Lesson


class TestLesson:
    # 这个课程功能模块，每一个接口都需要登录
    def setup_class(self):
        print('-------执行课程模块用例----开始-------')
        session = Login().api_login('auto','sdfsdfsdf')[0]
        print('-------执行课程模块用例----结束-------')

    def test_add_lesson(self,session,inData):
        print('-------执行课程模块用例----开始-------')
        res = Lesson().addLesson(session,inData)
        assert json.loads(res)['retcode'] == 0
        print('-------执行课程模块用例----结束-------')
