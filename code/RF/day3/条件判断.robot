*** Test Cases ***
条件判断1
  ${date}  get time
  log to console  ${date}
  should contain  ${date}  2020
  run keyword if  '2020' in $date  log to console  '今年是2020'

条件判断2
  ${date}  get time
  run keyword if  '06' in $date  log to console  当前时间是6月
  ...         ELSE  log to console  当前时间是2020

条件判断3
  ${date}  get time
  run keyword if  '06' in $date  log to console  当前时间是6月
  ...         ELSE IF  '07' in $date  log to console  当前时间是7月
  ...         ELSE  log to console  当前时间是2020年

条件判断4-赋值操作
   # 如果当前时间是7月，就把当前时间赋值给一个变量
   ${date}  get time
   ${var}  set variable if  '07' in $date   ${date}
   log to console  ${var}