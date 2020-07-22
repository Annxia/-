*** Test Cases ***
case1-login
    [Template]  login-kw
    #用例主体部分全部为模板关键字的参数
    user1  12345  success
    user2  abc  success
    user3  123456  fail

*** Keywords ***
login-kw
    [Arguments]  ${name}  ${password}  ${expect}
    log to console  输入用户名${name}
    log to console  输入密码${password}
    log to console  检查结果${expect}
    should be equal  ${expect}  success