*** Settings ***
Library  SeleniumLibrary
Variables  pylib/conf.py

#*** Variables ***
#${test_env}  http://localhost/mgr/login/login.html
#@{user1}  auto  sdfsdfsdf
#&{user2}  name=auto  psw=sdfsdfsdf

*** Keywords ***
deleteAllTeacher
    # 开始登录
#    loginwebsite

    # 点击进入老师菜单
    click element  css=[ui-sref="teacher"]

    # 删除所有老师
    set selenium implicit wait  2
    FOR  ${i}  IN RANGE  9999
        ${del_btns}   get webelements  css=[ng-click="delOne(one)"
        exit for loop if  $del_btns==[]
        click element   ${del_btns}[0]
        click element  css=.btn-primary
        sleep  1
    END

deleteAllLesson

    # 开始登录
#    loginwebsite

    # 点击进入课程菜单
    click element  css=[ui-sref="course"]

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
    # 点击进入课程菜单
    click element  css=[ui-sref="course"]
    # 完成添加课程
    [Arguments]  ${name}  ${desc}  ${idx}
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]  ${name}
    input text  css=[ng-model="addData.desc"]  ${desc}
    input text  css=[ng-model="addData.display_idx"]  ${idx}
    click element  css=[ng-click="addOne()"]
    sleep  1

addTeacher
    # 点击进入课程菜单
    click element  css=[ui-sref="teacher"]
    # 完成添加老师
    [Arguments]  ${realname}  ${username}  ${desc}  ${idx}  ${course}

    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addEditData.realname"]  ${realname}
    input text  css=[ng-model="addEditData.username"]  ${username}
    input text  css=[ng-model="addEditData.desc"]  ${desc}
    input text  css=[ng-model="addEditData.display_idx"]  ${idx}
    select from list by label  css=[ng-model*="courseSelected"]   ${course}
    click element  css=[ng-click*="addTeachCourse"]
    click element  css=[ng-click="addOne()"]
    sleep  1

checkCourse
    # 检查课程
    [Arguments]  @{expect}   # 类似于python的*args
    # 点击进入课程菜单
    click element  css=[ui-sref="course"]
    ${courses}  get webelements  css=tbody td:nth-child(2)
    ${res}  evaluate  [course.text for course in $courses]
    log   ${expect}
    should be true  $res==$expect

checkTeacher
    # 检查课程
    [Arguments]  @{expect}   # 类似于python的*args
    # 点击进入课程菜单
    click element  css=[ui-sref="teacher"]
    ${teachers}  get webelements  css=tbody td:nth-child(3)
    ${res}  evaluate  [teacher.text for teacher in $teachers]
    log   ${expect}
    should be true  $res==$expect


WebSetup
    open browser  http://localhost  chrome
    set selenium implicit wait  10

WebTeardown
    close browser
