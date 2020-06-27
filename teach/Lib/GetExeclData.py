import xlrd


def get_execlData(sheetName, startRow, endRow, bodyCol, repsCol):
    '''

    :param sheetName: 表名
    :param startRow: 开始行数
    :param endRow: 结束行数
    :param bodyCol: 请求体列数
    :param repsCol: 响应体列数
    :return: [(请求体，响应体),(请求体，响应体)]
    '''
    execlDir = "../data/松勤-教管系统接口测试用例-v1.4.xls"
    workBook = xlrd.open_workbook(execlDir, formatting_info=True)
    workSheet = workBook.sheet_by_name(sheetName)
    dataList = []
    for cnt in range(startRow-1, endRow):
        params = workSheet.cell_value(cnt, bodyCol)  # 请求体
        result = workSheet.cell_value(cnt, repsCol) #预期结果
        dataList.append((params, result))
    return dataList