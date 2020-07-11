# 用例   ---注释写法和python一样

# 定义一个表头,可以自动提示,注意单词首字母大小写 用空格间隔
*** Test Cases ***
# 写用例名需顶格写
用例1
# 用例步骤-和边上至少空两格
  # 用例的主体是关键字，每个步骤用一个关键字表示，通常以关键字开头
  log to console  hello robot
  # 关键字与参数之间，参数与参数之间需要定义间隔----两个以上空格
  log to console  hello 123545
  fail

# 多个用例可以放在同一个表里
用例2
   [Tags]  回归测试
   [Setup]  log to console  初始化
   [Teardown]  log to console  清除
   log to console  执行用例2


# 纯文本文件--svn/git 擅长管理文本类型文件
# 指定用例运行--- robot -t 用例名 测试文件/目录
