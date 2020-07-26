*** Settings ***
Library  SeleniumLibrary
Variables  conf.py

#*** Variables ***
#${test_env}  http://localhost/mgr/login/login.html
#@{user1}  auto  sdfsdfsdf
#&{user2}  name=auto  psw=sdfsdfsdf

*** Keywords ***
deleteAllLesson

    # 开始登录
    loginwebsite

    # 删除所有课程
    set selenium implicit wait  2
    FOR  ${i}  IN RANGE  9999
        ${del_btns}   get webelements  css=[ng-click="delOne(one)"
        exit for loop if  $del_btns==[]
        click element   ${del_btns}[0]
        click element  css=.btn-primary
        sleep  1
    END


loginwebsite
     # 登录操作
    go to  ${test_env}
#    input text  id=username  ${user1}[0]
#    input text  id=password  ${user1}[1]
    input text  id=username  ${user2}[name]
    input text  id=password  ${user2}[psw]
    click element  css=.btn-success

addCourse
    # 完成添加课程
    [Arguments]  ${name}  ${desc}  ${idx}
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]  ${name}
    input text  css=[ng-model="addData.desc"]  ${desc}
    input text  css=[ng-model="addData.display_idx"]  ${idx}
    click element  css=[ng-click="addOne()"]
    sleep  1

checkCourse
    # 检查课程
    [Arguments]  @{expect}   # 类似于python的*args
    ${courses}  get webelements  css=tbody td:nth-child(2)
    ${res}  evaluate  [course.text for course in $courses]
    log   ${expect}
    should be true  $res==$expect

WebSetup
    open browser  http://localhost  chrome
    set selenium implicit wait  10

WebTeardown
    close browser
