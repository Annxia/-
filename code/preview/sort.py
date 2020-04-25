alist = [9, 2, 6, 0]

# 冒泡排序
# 找n-1次较大值，两两相邻元素对比，大往后移
for i in range(0, len(alist) - 1):
    # 每一次的较大值---相邻比较
    # i=0 j=0 1 2;
    for j in range(0, len(alist) - 1 - i):
        # if 前者>后者 交换位置
        if alist[j] > alist[j + 1]:
            alist[j], alist[j + 1] = alist[j + 1], alist[j]
print(alist)