# init文件名不能写错

*** Settings ***
#需要重新导入关键字库
Library  SeleniumLibrary


Suite Setup  open browser   http://www.baidu.com  chrome
Suite Teardown  close browser

Test Setup  log to console  &&&执行默认初始化
Test Teardown  log to console  &&&执行默认清除