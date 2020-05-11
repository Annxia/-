from pprint import pprint


def putInfoToDict(fileName):
    resdict = {}
    with open(fileName) as file:
        lines = file.read().splitlines()
        for line in lines:
            line = line.replace('(', '').replace('),', '').replace(');', '').strip()
            id = int(line.split(',')[2])
            lessonid = line.split(',')[1]
            checkintime = line.split(',')[0].replace("'", '')

            info = {'lessonid': lessonid, 'checkintime': checkintime}
            if id in resdict:
                resdict[id].append(info)
            else:
                resdict[id] = [info]

        return resdict


fileDir = r'D:\learn-automated-testing\code\resources\0005_1.txt'
dict = putInfoToDict(fileDir)
pprint(dict)