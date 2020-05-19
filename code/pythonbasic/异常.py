print('---lesson_24 异常----')
''''
工作任务：web ui 自动化（脚本） 给了10个场景用例，要求早上下班前告诉哪些可以通过？
执行方案：
    A：从第一个开始 慢慢测 
        场景3，某一个元素定位失败--修改代码
    B:采用异常机制：

'''
'''
接口自动化---python---自动化执行excel测试用例---结果写到报告里
10个用例：第5个用例报错---后续的用例直接不能运行

异常处理的目标：代码出现问题，不让代码停止，继续运行，我们可以来处理这个异常！

方案一：比喻：防火墙
    事前处理：if判断：未卜先知-----要写if后面跟着的条件是已知
    缺点：如果出现没有预料到的异常，报错

方案二：人体免疫系统---异常机制
    事后处理：出现问题，我们来处理---解决问题

'''

#
# import traceback
# while True:
#     num = input('input a number:')
#     try:#捕获下面语句的异常
#         print ('100 / %s = %s' % (num, 100.0/int(num)))
#
#     # except ZeroDivisionError:#一种已知的异常，其他异常不能处理
#     #     print('除数不能为0 ，重新输入！')
#     #
#     # except ValueError as error:
#     #     print('除数为数字！',error)
#
#     # except Exception :#未知的异常
#     #     print('异常了，处理异常')
#
#     except:#except Exception简写
#         print('异常了，处理异常',traceback.format_exc())#详细的报错信息

try:
    fo = open('xxx')
except:
    print('文件不存在！！！')

'''
12306刷票----网络不好的时候，就有些元素定位失败，元素就不能操作--就报语法错误

'''


def f3():  # 区
    print('in f3 - begin')
    b = 4 / 0
    print('in f3 - end')


def f2():  # 市
    print('in f2 - begin')
    f3()
    print('in f2 - end')


def f1():  # 省
    print('in f1 - begin')
    f2()
    print('in f1 - end')


# f1()


# fo = open('xxx')


'''
函数嵌套调用：就好比，政策发布： 上---下
异常的抛出：下---上
异常在哪一层处理：谁合适谁处理！
举例：
    项目接口A  ---外包开发团队--已经交付--尾款已收
    甲方使用这个接口的时候可能出问题，酌情处理！

场景：
    1- 在我们使用一些第三方库的时候，调用了一个方法，会出现很多条报错信息-怎么解决？
    解决方案：不要慌！
    分析：
        1- 第一条报错信息，是你直接调用方法的那行
        2- 最后一行：这个报错的根本原因(不一定很直观)
        3- 排查第一行报错信息的传参个数与类型--与定义的对比
        4- 建议：报错看第一行报错+最后的一行还有具体的报错详情
'''


#
# 断言 assert---检查点-----如果后续代码比较重要，而且很依靠前面的数据或者状态
# tel = input('请输入手机号：')
# assert len(tel) == 11,'手机位数有误！'
#
# print('我在处理手机运营商操作')
# --对手机号进行供应商鉴open
# 自定义异常-----name 过长异常--继承

class UserValueError(Exception):
    print('')


class NameTooLongError(Exception):
    err = 'name.long'
    print('NameTooLongError')

    def methFun(self):
        pass


# 自定义异常-----name 过短异常--继承
class NameTooShortError(Exception):
    print('NameTooShortError')


def inputName():
    name = input('请输入用户名：')  # 5-10
    if len(name) > 10:
        raise NameTooLongError  # 自定义的异常要自行抛出
    elif len(name) < 5:
        raise NameTooShortError


try:
    inputName()
except NameTooShortError:
    print('您输入的用户名太短！')
except NameTooLongError as e:
    print('您输入的用户名太长！', e.err)
    e.methFun()

'''
'''

