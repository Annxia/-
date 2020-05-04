def caculate(list):
    list1 = []
    idx = 0
    for i in list:
        list1.append(sum(list[:idx + 1]))
        idx += 1

    return list1


print(caculate([1, 2, 3, 4]))
