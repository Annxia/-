*** Settings ***
Library  testlib.py

*** Test Cases ***
常用关键字
  log   今天上RF
  log to console  今天上RF
  log many  今天  天气  很好
  # 字符串包含多个空格的临时解决方法：从第二个空格处用反斜杠\修饰
  log many  今天 \ 天气  很好

传递参数1
  # 定义变量
  ${var}  set variable  2020
  ${type}  get type  ${var}
  log to console  ${type}
  ${res}  get num  10
  log to console  ${res}
  # 定义一个浮点数类型变量
  ${num}  convert to number  2020
  log to console  ${num}
  # 定义一个整数类型变量
  ${int}  convert to integer  2020

  # 直接转化整数的方法
  ${res}  get num  ${2020}
  log to console  ${res}

常见关键字-断言
    ${expect}  set variable  2020
    should be equal  ${expect}  2020
    should be equal as integers  ${expect}  2020

    # RF变量表示的字符串传递给python时会去掉引号
    ${test}  set variable  hello
    should be true  'hello'=='${test}'
    should be true  'hello'==$test

    #表达式不能有两个以上的空格
    should be true  'he' in 'hello'


