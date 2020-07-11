*** Settings ***
#套件配置区，可以用来导入该测试套件下需要用到的第三方关键字库
Library  SeleniumLibrary    # 库名大小写敏感，一行只能导入一个库

# 定义表头
*** Test Cases ***

# 用例名顶格
百度搜索松勤
  # 打开浏览器--- 需手动配置webdriver路径到环境变量PATH
  open browser  http://www.baidu.com  chrome
  # 设置全局隐式等待时间
  set selenium implicit wait  10
  # 输入松勤
  input text  id=kw  松勤\n
  # 获取文本---变量
  ${res}  get text  id=1
  # 断言
  should contain   ${res}  松勤网 - 松勤软件测试
  # 关闭浏览器
  close browser


