# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 列表元组.py
# @ide: PyCharm
# @time: 2020/8/13 11:34
'''
    1- 列表：
     1.列表也是序列类型 ：
        1-有编号--下标
        2-能切片
     2.能存储任意类型
'''
#1- 列表的定义
alist = [10,3.14,'hello', [100,200]]

# 列表获取元素 --下标
print(alist[-1][-1])

# 2- 200不在列表里
print(200 in alist[-1])

# 修改值
alist[0] = 20

# 增加元素
# append--在列表尾部增加元素
alist.append(300)
# insert-- 插入(下标，值)
# 如果insert的下标>列表长度len(),效果就等同于append
alist.insert(0,20)

# 删除操作
alist1 = [10,20,30,40]
# del  序列类型，删除一个后会自动重新排序
del alist1[1],alist1[2]   # [10,30]
del alist1[1:1+2]  # [10,40]

# pop 也使用下标  有返回值-被删元素值
res = alist1.pop[1]
print(res)

# remove --三种删除方法中最慢的一种，一次只能删一个元素
alist2 = [10,20,30,40,20]
alist2.remove(20) # 直接删值----值不清楚在哪里，得去匹配删除
# 如果这个值不存在，remove会报错
# 只要这个元素在，就一直删，如果元素已经不在，不能删
while 20 in alist2:
    alist1.remove(20)

# 清空列表
alist1.clear()

#5- 合并
a = [10,20,30]
#  临时合并
print(a+[50,60]) # 不改变源对象，新对象另存新地址--id() 查看对象地址

# 列表扩展--在原有地址进行扩展
a.extend([40,50])
print(a)

# 总结：
'''
    列表是可变化的  ---元素的值可以改变： 元素的个数可以改变
    使用场景：
        1- 存储类型
        2- 有序的，可以增加删除的  环境变量path
            import sys
            print(sys.path)
'''

'''
    元组：
    1 序列类型：有下标 切片
    2 可以存放任意类型
    3 一个元素 （1,)
    4 不支持修改：元素值和个数都不能改
    使用场景：
    1- 一些不希望别人去修改的参数
        systemConfigData = ()
        优化：
            参数可以部分支持修改
            systemConfigData_t = (10,[])
'''

tul = (10,20)
print(list(tul)) # 转化另存为一个列表 不改变源元组
print(tul)