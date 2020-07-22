*** Test Cases ***
case1
  # 参数本质是字符串--内容是python语法表达式
  ${list}  evaluate  [i for i in range(100)]
  log to console  ${list}
  ${list2}  create list  1
#  evaluate  ${list2[-1] = ${list[-1]  ---执行错误，eval不支持赋值操作