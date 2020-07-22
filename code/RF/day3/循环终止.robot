*** Settings ***
Library  testdemo
Library  Dialogs

*** Test Cases ***
循环终止1
  FOR  ${i}  IN RANGE  999
  # 条件成立终止循环
  run keyword if  $i>100  exit for loop
  log to console  ${i}
  END

循环终止2
  # 将字符串类型转换成int
  check score  ${61}

循环终止3
    FOR  ${i}  IN RANGE   999
    ${score}  get value from user  请输入分数
    run keyword if  ${score}=='continue'  continue for loop
    run keyword if  ${score}=='exit'  exit for loop
    check score  ${score}
    END

循环终止4
    FOR  ${i}  IN RANGE   999
    ${score}  get value from user  请输入分数
    continue for loop if  if  ${score}=='continue'
    exit for loop if  ${score}=='exit'
    check score  ${score}
    END