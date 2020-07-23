#RF本身也同意pythonpath是Python文件，所以导入python文件时会统一pythonpath
#如果导入的库文件引用了其他自定义库，确保被引用的库也要处于pythonpath里

*** Settings ***
Library  task.stu_lib

*** Test Cases ***
case1
    ${user}  get user
    log to console  ${user}