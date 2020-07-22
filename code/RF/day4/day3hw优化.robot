创建一个RF测试套件，包含下面的一个用例


用例名：
验证当系统中没有课程的时候，是否能成功添加一个课程

前置条件：
系统中没有课程

测试步骤：
添加课程，输入课程名、详情描述、展示次序，点击创建

预期结果：
创建的课程正确显示在下面的课程列表中。
这里为了简化，我们只检查 课程名就可以了


注意：
这个用例的初始化和清除操作，都是需要设置为无课程状态。
需要我们开发一个python测试库，使用selenium库开发关键字函数deleteAllCourse， 实现使用Python自动点击删除课程按钮

*** Settings ***
Library  SeleniumLibrary
Library  course_lib

*** Test Cases ***
添加课程
    [Setup]  deleteAllLesson

    loginwebsite
    addCourse  selenium  webUI课程  1
    checkCourse  selenium

    close browser

*** Keywords ***
loginwebsite
     # 登录操作
    open browser  http://localhost/mgr/login/login.html  chrome
    set selenium implicit wait  10
    input text  id=username  auto
    input text  id=password  sdfsdfsdf
    click element  css=.btn-success

addCourse
    # 完成添加课程
    [Arguments]  ${name}  ${desc}  ${idx}
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]  ${name}
    input text  css=[ng-model="addData.desc"]  ${desc}
    input text  css=[ng-model="addData.display_idx"]  ${idx}
    click element  css=[ng-click="addOne()"]

checkCourse
    # 检查课程
    [Arguments]  ${exepect}
    ${courses}  get webelements  css=tbody td:nth-child(2)
    ${res}  evaluate  [course.text for course in $courses]
    should be true  $res==[$exepect]
