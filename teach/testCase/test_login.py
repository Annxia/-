import json
from Lib.ApiLogin import Login


class TestLogin:
    def test_Login(self):
        res = Login().api_login('auto','sdfsdfsdf')[1]
        print(res)
        assert json.loads(res)['retcode'] == 0