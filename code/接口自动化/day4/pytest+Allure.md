#### pytest
1. pytest框架简介
    - 纯python代码的自动化测试框架
    - 安装
        - pip install pytest
        - pip show pytest
    - Pytest框架注意事项
        - .py测试文件必须以test_开头(或者以_test结尾)
        - 测试类必须以Test开头，并且不能有init方法
        - 测试方法必须以test开头
        - 断言必须使用assert
    - 搭建项目
        - testcase ---测试用例代码
        - Lib ---库---模块
        - 报告：log/html
        - data ---测试用例文件
        - config ---配置文件

2. 操作流程
    - pytest环境搭建
    - 怎么运行一个函数封装的用例
        pytest xx.py -s   -s输出print信息       
    - 怎么运行一个类封装的用例  
    - 怎么生成报告----pytest-html        
        pip intsall pytest-html  
        pytest xx.py -s --html=report.html
    - 需要做自动化测试
        - 环境初始化
        - 数据清除
    - 封装类
        
3. pytest数据驱动
    1. 基本语法：   
    `@pytest.mark.parametrize('x,y',[(1,2),(3,4),(5,6)])`
    