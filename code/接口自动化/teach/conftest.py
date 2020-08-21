import json

import pytest

from Lib.ApiLesson import LessonClass
from Lib.ApiLogin import LoginClass


@pytest.fixture(scope='module', autouse=True) #初始化
def delete_all_lesson(request):
    # 1- 登录
    session = LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}')
    # 2- 列出所有课程
    inData = {'action':'list_course',
              'pagenum':'1',
              'pagesize':'20'}
    resList = json.loads(LessonClass().list_lesson(session, inData))['retlist']
    # 3- 删除所有课程
    while resList!=[]:
        for one in resList:
            lessonId = one['id']
            LessonClass().delete_lesson(session, lessonId)
        resList = json.loads(LessonClass().list_lesson(session, inData))['retlist']

    # 创建课程的测试数据
    for one in range(1, 7):
        lessonData = {
                  "name":f"初中化学{one:0>3}",
                  "desc":"初中化学课程",
                  "display_idx":f"{one}"
        }
        LessonClass().add_lesson(session, lessonData)

    # 环境数据清除 -----teardown
    def fin():
        print('--------测试环境恢复-----------')

    request.addfinalizer(fin)