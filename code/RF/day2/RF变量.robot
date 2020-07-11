*** Test Cases ***
列表类型
  ${list}  create list  a  b  c
  log many  ${list} # 整体传参
  log many  @{list} # 拆包传参--多个
  log many  ${list}[1]
  log many  ${list[1]}

列表类型2
  @{list}  create list  a  b  c
  log many  ${list} # 整体传参
  log many  @{list} # 拆包传参--多个
  log many  ${list}[1]

字典类型
   ${dict}  create dictionary  a=1  b=2  c=3
   log many  ${dict}
   log many  &{dict}
   log to console  ${dict}[a]
#   log to console  ${dict['a']}