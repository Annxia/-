*** Settings ***
# 表示强制给该套件下面所有用例都打上标签
Force Tags  回归测试   webAPI

*** Test Cases ***
case1
    [Tags]  功能点1  回归测试   webAPI
    log to console  执行测试用例1

case2
    [Tags]  功能点1  回归测试  webAPI
    log to console  执行测试用例1

case3
    [Tags]  功能点1  回归测试  webAPI
    log to console  执行测试用例1


# 指定标签运行  robot --include tag datasource