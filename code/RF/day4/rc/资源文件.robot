资源文件解决的问题：
在测试套件文件中定义关键字的问题
只能在本测试套件中有效，无法共享给其他测试套件使用

使用资源文件
资源文件就是RF层面的库文件(不能包含测试用例表)
里面可以包含用来共享的 变量和关键字
资源文件的格式基本 也和 测试套件文件 类似

*** Keywords ***
用户关键字1
    log to console  这是一个用户关键字

用户关键字2
    #形参
    [Arguments]  ${arg1}
    ${res}  set variable  hello  ${arg1}
    log to console  ${res}

用户关键字3
    #形参
    [Arguments]  ${arg1}
    ${res}  set variable  hello  ${arg1}
    log to console  ${res}
    [Return]  RF课程#####
