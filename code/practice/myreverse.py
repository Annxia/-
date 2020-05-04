def myreverse(list):
    list1 = []
    for i in range(len(list)):
        list1.append(list.pop(len(list)-1))

    print(list1)


myreverse([])