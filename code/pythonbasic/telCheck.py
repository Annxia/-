from tkinter import *
from tkinter import messagebox # python3.0的messagebox，属于tkinter的一个组件
import re,requests

def select(tel):
    if tel.isdigit():
        if len(tel) == 11:
            url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
            #不写 .decode('UTF-8')  得到的html_content会出现不少中文的编码，一定得加
            html_content = requests.post(url, data={"mobileCode": tel, "userID": ""}).content.decode('UTF-8')
            message = re.findall('<string xmlns="http://WebXml.com.cn/">(.+?)</string>', html_content, re.S)[0]
        else:
            message = '您输入的手机号码位数错误！'
    else:
        message='您输入的手机号码有非法字符！'
    return message

#窗口创建
top = Tk()#创建tk对象
top.title("松勤自动化班-Python-查号系统")#标题
# top.iconbitmap(r'G:\333.ico')
top.geometry('300x150')  # 是x 不是*   框大小

#输入框创建
text = Label(top, text="请输入查询的手机号码：")
text.pack(side=TOP)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()#获取输入
xls = Entry(top, textvariable = xls_text)#输入控件；用于显示简单的文本内容
xls_text.set(" ")#设置默认的内容
xls.pack()#包装

def click():
    message = select(xls_text.get().strip())
    messagebox._show(title='查询结果：', message=message)

#包装一个按钮
Button(top, text="查号！", fg="blue", bd=2, width=6, command=click).pack()
#运行
top.mainloop()



