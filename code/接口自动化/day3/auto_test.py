#------python操作execl---------
#1-  读取用例 ----参数化-----
#常用的库：openpyxl / xlrd xlwt  xlutils
import json
import xlrd #读取库
from xlutils.copy import copy

from 接口自动化.day3.api_login import login

execlDir = r'D:\松勤学习\22-接口自动化\松勤-教管系统接口测试用例-v1.4.xls'
#1- 打开execl
#formatting_info=True 保持execl样式，不支持xlsx
workBook = xlrd.open_workbook(execlDir, formatting_info=True)
# sheetNames = workBook.sheet_names()# 所有的表名--列表
# print(sheetNames)

#2- 操作对应的用例表
workSheet = workBook.sheet_by_name('1_登录接口')# 通过表名获取
# workSheet = workBook.sheet_by_index(1) #通过下标获取
# 2-  写用例 ----测试结果-----
# 1-在缓存里copy一个新的execl对象，不影响源数据用例
new_workBook = copy(workBook)
new_workSheet = new_workBook.get_sheet(1)  # 新的表

#3- 读取：一行 一列 单元格
#1 一行
# rowData = workSheet.row_values(1)
# print(rowData)

#2 一列
# colData = workSheet.col_values(0)
# print(colData)
def login_auto(row):
    #3 单元格
    cellData = workSheet.cell_value(row,6)#字符串类型
    cellExp = json.loads(cellData)
    tc_id = workSheet.cell_value(row, 0) #用例编号
    resultExp = json.loads(workSheet.cell_value(row,8))['retcode']#预期结果

    # 传递参数
    res = json.loads(login(cellExp['username'],cellExp['password']))
    #2-判断测试用例是否通过----断言 assert

    if res['retcode'] == resultExp:
        print(f'{tc_id}-----pass----msg:{res}')
        info = 'pass'
    else:
        print(f'{tc_id}-----fail----msg:{res}')
        info = 'fail'

    new_workSheet.write(row,9,info)


for cnt in range(1,5):
    login_auto(cnt)

new_workBook.save(r'./res.xls')
