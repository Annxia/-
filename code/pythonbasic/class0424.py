# def r():
#     str = 'abcdefea'
#     idx = 0
#     restr = []
#     start = 0
#     while idx != -1:
#         idx = str.find('x',start)
#         start = idx +1
#         if idx != -1:
#             restr.append(idx)
#
#     print(restr)
#
# a = max(34,67,22,11,88)
# b = max([34,67,22,11,88])
# c = max((34,67,22,11,88))
# print(a,b,c)
# print(type(r()))

# def t2(para):
#     para = 3
#
# b = [1]
# t2(b)
# print(b)
# print('hi,jack,you are smart,jack'.replace('jack','Ann',2))


# def func(**kwargs):  # ** 封装成字典
#     print(kwargs)
#
#
# func(name='tom')  # 函数传值的时候一定要 键值 格式：变量名 = 值
def func(a, b, c=0, *args, **kw):
    print(f'a={a}, b={b}, c={c}, args={args}, kw={kw}')

func(1, 2, 3, 5)