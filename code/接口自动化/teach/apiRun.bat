cd D:\learn-automated-testing\teach\testCase
pytest -sq --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
