*** Test Cases ***
循环1
  # 循环语法
  FOR  ${i}  IN  a  b  c  d  e
  log to console  ${i}  # 循环体
  END

循环2
  ${list}  create list  a  b  c  d  e
  FOR  ${i}  IN  @{list}
  log to console  ${i}
  END

循环3
  FOR  ${i}  IN RANGE  10
  log to console  ${i}
  END

循环4
  FOR  ${i}  IN RANGE  1  11
  log to console  ${i}
  END

循环5
  FOR  ${i}  IN RANGE  1  11  2
  log to console  ${i}
  END