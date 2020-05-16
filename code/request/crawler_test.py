#设置读取网页的头部，该行代码主要用于模拟浏览器来访问网站
user_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#https://search.51job.com/
#51job
import requests,re
from test.excel_demo  import excel_init
wookBook,wookSheet = excel_init()

def get_pageNum():
    web_url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url, headers=user_header)
    resp.encoding = 'gbk'
    pageNum = re.findall('<span class="td">共(.*?)页，到第</span>',resp.text,re.S)[0].strip()
    return int(pageNum)


print('-------------页数：',get_pageNum())
num = 1
#-----------------------1、构建请求-------------------
for page in range(1,get_pageNum()+1):# 1- 29+1
    web_url = f'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,{page}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url,headers = user_header)
    #查看发出去请求头
    # print(resp.request.headers)
    #-----------------------2、解析响应-------------------
    resp.encoding = 'gbk'
    # print(resp.text)#字符串格式返回

    #-----------------------3、提取数据-------------------
    '''
    <div class="el">
            <p class="t1 ">
                <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
                <input class="checkbox" type="checkbox" name="delivery_jobid" value="121199339" jt="0" style="display:none">
                <span>
                    <a target="_blank" title="自动化测试工程师" href="https://jobs.51job.com/shanghai/121199339.html?s=01&amp;t=0" onmousedown="">
                        自动化测试工程师                </a>
                </span>
                                                                        </p>
            <span class="t2"><a target="_blank" title="上海慧管信息技术有限公司" href="https://jobs.51job.com/all/co3785077.html">上海慧管信息技术有限公司</a></span>
            <span class="t3">上海</span>
            <span class="t4">1-1.5万/月</span>
            <span class="t5">05-15</span>
        </div>
    
    
    '''
    #1- 获取这个页面所有的el
    lines = re.findall('<div class="el">(.*?)</div>',resp.text,re.S)
    #2- 对每一行进行操作--提取更细的需求

    for line in lines:
        temp = re.findall('<a target="_blank" title="(.*?)" href',line,re.S)
        #1- 岗位名称
        jobName = temp[0].strip()
        wookSheet.write(num,0,jobName)
        #2- 公司名称
        company = temp[1].strip()
        wookSheet.write(num, 1, company)
        #3- 地址
        address = re.findall('<span class="t3">(.*?)</span>',line,re.S)[0].strip()
        wookSheet.write(num, 2, address)
        #4- 薪资
        salary = re.findall('<span class="t4">(.*?)</span>', line, re.S)[0].strip()
        wookSheet.write(num, 3, salary)
        #5- 发布时间
        jobTime = re.findall('<span class="t5">(.*?)</span>', line, re.S)[0].strip()
        wookSheet.write(num, 4, jobTime)

        num += 1#换行
#-----------------------4、保存excel-------------------
wookBook.save(r'.\res_51job.xls')

'''
1- https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
2- https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
3- https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,3.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=




'''