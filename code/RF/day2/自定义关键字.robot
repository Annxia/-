*** Settings ***
# Library  testlib2.py    # 路径导入法
Library  testlib2       # 模块导入法--遵循python导入规则-------robot -P . 自定义关键字.robot


*** Test Cases ***
获取课程
    ${course}  get course
    log to console  ${course}