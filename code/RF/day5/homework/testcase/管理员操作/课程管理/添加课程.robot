用例：检查添加课程功能

前置条件：系统中没有课程，

步骤 1： 添加课程，输入课程名、详情描述、展示次序为2，点击创建
预期结果：创建的课程正确显示在下面的表中。

步骤 2： 再添加一门课程，输入课程名、详情描述、展示次序为1，点击创建
预期结果：创建的课程正确显示在下面的表中，并且按照展示次序排列。


这里为了简化，我们只检查 课程名就可以了

要求：
将用例中的 登录、添加课程、检查课程， 合理使用 资源文件里面的用户关键字  实现
如果可以，将初始化、清除操作 也改为用 用户关键字实现

*** Settings ***
Resource  rflib/rc.robot


*** Test Cases ***
添加课程
    [Setup]  deleteAllLesson

    addCourse  robotframe  RF课程   2
    checkCourse  robotframe

    addCourse  selenium  webUI课程  1
    checkCourse   selenium  robotframe





