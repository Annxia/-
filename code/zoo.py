from random import randint
from time import time


class Tiger:
    nickname = "tiger"

    def __init__(self, inWeight=200):
        self.weight = inWeight

    #叫
    def roar(self):
        print("老虎叫----Wow！")
        self.weight -= 5

    #吃
    def feed(self, food):
        #喂食正确--增加体重
        if food == 'meet':
            print("喂食正确，体重增加10斤！")
            self.weight += 10
        else:
            print("喂食错误，体重减少10斤！")
            self.weight -= 10


class Sheep:

    def __init__(self, inweight=100):
        self.weight = inweight

    def roar(self):
        print("羊叫---Mie!")
        self.weight -= 5

    def feed(self, food):
        # 喂食正确--增加体重
        if food == 'grass':
            print("喂食正确，体重增加10斤！")
            self.weight += 10
        else:
            print("喂食错误，体重减少10斤！")
            self.weight -= 10


class Room:
    def __init__(self, inNum, inAnimal):
        self.num = inNum
        self.animal = inAnimal


roomList = []
for one in range(1,11):
    if randint(0,1) == 1:
        ani = Tiger()
    else:
        ani = Sheep()
    room = (one,ani)
    roomList.append(room)

startTime = time()
while True:
    curTime = time()
    if curTime - startTime > 120:
        break
