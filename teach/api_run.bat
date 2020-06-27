@echo off
echo 松勤-教管系统接口自动化运行准备开始......
@echo on



del /f /s /q  D:\learn-automated-testing\teach\report\tmp\*.json
del /f /s /q  D:\learn-automated-testing\teach\report\tmp\*.jpg
del /f /s /q  D:\learn-automated-testing\teach\report\report



@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on


cd  D:\learn-automated-testing\teach\testCase
pytest  -sq --alluredir=../report/tmp
allure generate  ../report/tmp -o ../report/report --clean


@echo off
echo 接口自动化运行成功
pause

