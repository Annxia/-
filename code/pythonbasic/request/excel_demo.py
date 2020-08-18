# author：xintian   time:2020-04-15
import xlwt
def excel_init():
    '''
    :return:
    '''
    #----------------------1、创建excel文件对象---------------
    workBook = xlwt.Workbook(encoding='utf-8')
    #----------------------2、创建表-------------------------
    wookSheet = workBook.add_sheet('51job')
    #----------------------3、写样式--列名-------------------
    colNames = ['岗位名称','公司名称','地址','薪资','发布时间']
    for one in range(0,len(colNames)):#0 1 2 3 4
        wookSheet.write(0,one,colNames[one])#(行号，列号，内容)   行列号--从0开始

    return workBook ,wookSheet
    # #---------------4- 保存路径-------------------------------
    # workBook.save(fileDir)