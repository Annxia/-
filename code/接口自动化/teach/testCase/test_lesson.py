import json

import allure
import pytest

from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
from Lib.GetExeclData import get_execlData


@allure.feature('课程模块')
@pytest.mark.lesson(order=2)
class TestLesson:
    # 这个课程功能模块，每一个接口都需要登录
    def setup_class(self):
        print('-------登录模块----开始-------')
        self.session = LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}')
        print('-------登录模块----结束-------')

    @allure.story('新增课程')
    @pytest.mark.lesson_add
    @pytest.mark.parametrize('inData,repsData',get_execlData('2_课程-新增课程', 2, 26, 6, 8))
    def test_add_lesson(self, inData, repsData):
        res = LessonClass().add_lesson(self.session, json.loads(inData))
        assert json.loads(res)['retcode'] == json.loads(repsData)['code']

    @allure.story('列出课程')
    @pytest.mark.lesson_list
    @pytest.mark.parametrize('inData,repsData',get_execlData('2_课程-列出课程', 2, 13, 6, 8))
    def test_list_lesson(self, inData, repsData):
        res = LessonClass().list_lesson(self.session, json.loads(inData))
        assert json.loads(res)['retcode'] == json.loads(repsData)['code']

    @allure.story('删除课程')
    @pytest.mark.lesson_delete
    @pytest.mark.parametrize('inData,repsData', get_execlData('2_课程_删除课程', 2, 9, 6, 8))
    def test_delete_lesson(self, inData, repsData):
        res = LessonClass().delete_lesson(self.session, json.loads(inData))
        assert json.loads(res)['retcode'] == json.loads(repsData)['code']


