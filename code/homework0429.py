resList = []


def putRecordToTable(fileType, fileLen):
    inFlag = False
    for one in resList:
        if one[0] == fileType: # 如果在的话，就累加大小
            one[1] += fileLen
            inFlag = True
            break

    if inFlag == False:
        resList.append([fileType,fileLen])

    return resList


with open(r"D:\learn-automated-testing\code\resources\log.txt") as fo:
    lines = fo.read().splitlines()
    del lines[0], lines[-1]

    for info in lines:
        if info.strip() == '':
            continue

        oneinfo = info.split("\t")
        name, size = oneinfo[:2]
        ext = name.split('.')[-1]
        putRecordToTable(ext,int(size))

print(resList)
