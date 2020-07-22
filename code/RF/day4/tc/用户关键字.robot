语法：由RF层面的关键字组成

作用：类似于RF层面的函数，用于封装一些步骤

1.如何定义RF关键字？----定义在keywords表中，语法和用例步骤相同
2.如何调用用户关键字？-----就当成普通的关键字调用

# 资源文件的搜索规则
1.根据指定的路径，从当前文件的相对路径的起点去寻找
2.根据指定的pythonpath为起点，根据导入的路径去寻找

*** Settings ***
#导入方式一：day4目录下 robot tc
#Resource  ../rc/资源文件.robot   #必须写上资源文件的后缀名
#导入方式二：day4目录下 robot -P . tc
Resource  rc/资源文件.robot

*** Test Cases ***
case1
    用户关键字1
    用户关键字2  RF
    ${res}  用户关键字3   RF
    log to console  ${res}


