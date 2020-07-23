*** Settings ***
Library  testlib.lib1
Library  testlib.lib2.testlib
Library  testlib.lib2   #类名和模块名一致时可以省略类名

#导入类的时候相当于实例化一个对象
Library  testlib.lib2.lib3  localhost  3306
#Library  testlib/lib2.py  #如果是用路径法导入库，只能导入到模块这个级别（同名类）

*** Test Cases ***
case1
    ${list}  returnlist
    log to console  ${list}

case2
     ${list}  _returnlist2
    log to console  ${list}

case3
     ${list}  return list3
    log to console  ${list}

类关键字
    ${list}  getlist
    log to console  ${list}

类关键字2-与模块同名
    open browser  http://localhost/mgr/login/login.html
    sleep  5
    close browser

类关键字3-带参关键字
    connect_db