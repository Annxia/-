*** Settings ***
Library  course_mgr.py
Library  SeleniumLibrary    # 库名大小写敏感，一行只能导入一个库

*** Test Cases ***
列出课程
  ${text}  list course
  FOR  ${course}  IN  @{text}
  log   ${course}
  END


  FOR  ${num}  IN RANGE  1  7
  ${class}  create list  初中化学00${num}
  log to console  ${class}
  END

  should be equal  ${course}  @{class}

用例2
  # 打开浏览器
  open browser  https://www.vmall.com/index.html  chrome
  # 设置全局隐式等待时间
  set selenium implicit wait  10
  ${eles}=  Get WebElements  css=.span-968 .grid-title
  FOR  ${ele}  IN  @{eles}
  log  ${ele.text}
  log to console  ${ele.text}
  END

  close browser



