# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 对象方法.py
# @ide: PyCharm
# @time: 2020/8/13 16:18
print("---")
'''
    1- 函数调用   函数名（）
    2- 方法：
        1- 一切皆为对象
            属性--特征
            方法--行为
        2- 到底什么是方法？  def不顶格，在一个class里面
            函数是属于xx.py   模块的
            方法 属于一个类
'''
# 字符串方法
# 1- count计算字符串中包含多少个指定的子字符串
str1 = 'abcde'
print(str1.count('a')) # 有返回值--int

# 2- endswith 检查字符串是否以指定的字符串结尾
tel = input('请输入手机号')
if tel.endswith('123'):
    print('幸运观众')

# 3- find 返回指定的子字符串在字符串中出现的位置-- 不知道有没有--未知结果
# 返回该元素所在的下标，每一次只能找一个，找不到返回-1
str2 = 'abcdeabc'
print(str2.find('a'))
if str2.find('b') != -1:
    print('有这个元素')

# 找出这个字符串中所有这个字符的下标
idx = 0
start = 0
resList = []
while idx != -1:
    idx = str2.find('a',start)
    start = idx+1
    if idx != -1:
        resList.append(idx)
print(resList)

#4- split 将字符串分割为几个子字符串
str3 = 'abcabc'
print(str3.split('b')) # 返回是一个列表，切点会被删除
# strip() ---去掉两边的空格,中间不能操作
print(str3.strip('x'))

# 5-replace 新 替换 旧
print(str2.replace('a','x')) # 默认全部替换
print(str2)