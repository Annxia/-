*** Settings ***
Library  SeleniumLibrary

# 定义套件级别的初始化和清除
Suite Setup   log to console   执行套件级别初始化
Suite Teardown  log to console   执行套件级别清除

# 作用在当前范围内，测试用例自身没有初始化清除的用例上
Test Setup  log to console  ~~~执行默认初始化
Test Teardown  log to console  ~~~执行默认清除

#测试用例级别的初始化与清除
*** Test Cases ***
case1
  [Setup]  log to console  执行用例初始化
  [Teardown]  log to console  执行用例清除
  log to console  执行用例主体部分

case2
  log to console  用例2
  input text  id=kw   songqin\n