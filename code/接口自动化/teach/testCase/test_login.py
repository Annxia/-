import json

import allure
import pytest
from Lib.ApiLogin import LoginClass
from Lib.GetYamlData import get_yaml_data


@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录接口')
    # @pytest.mark.parametrize('inData,repsData', get_execlData('1_登录接口', 2, 5, 6, 8))
    @pytest.mark.parametrize('inData,repsData', get_yaml_data())
    def test_Login(self, inData, repsData):
        res = LoginClass().api_login(inData, getSession=False)
        assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']