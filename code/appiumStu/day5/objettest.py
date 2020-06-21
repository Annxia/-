
class Obj():
    def __init__(self):
        print('初始化要执行的代码')

    def fun1(self):
        print('执行func1')

    def __del__(self):
        print('执行del')

if __name__ == '__main__':
    Obj().fun1()