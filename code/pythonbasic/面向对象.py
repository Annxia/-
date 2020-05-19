print('-----lesson-21+22-面向对象-----')


#对象：一切皆为对象  （int float  list  类 实例）
#1- 定义类
'''
函数：在一个模块里面 def xxx()-----函数调用  函数名()
方法：在类里面定义一个函数   调用   对象.方法名()
    1- 实例方法：这个方法跟实例相关---一般这个方法里有涉及实例属性
'''
# class Person:
#     nickName = '人类'#类属性--属于整个类的，每一个实例一样
#     def __init__(self,inName,inAge,inWeight):#不需要你来传的，会自动传实例进去
#         self.name = inName
#         self.age = inAge
#         self.weight = inWeight
#
#     #方法---实例方法:实例.实例方法
#     def eat(self):
#         print('我在吃-----')
#         self.weight += 10
#
#     #类方法：这个方法属于整个类--公有的行为
#     #类可以调用  实例也可以调用
#     @classmethod
#     def run(cls):
#         print('--------类方法')
#
#     #静态方法——可以没有任何参数    类/实例都可以调用
#     @staticmethod
#     def config():
#         print('-----静态方法')
#
#
#
# p1 = Person('tom',20,140)
# p2 = Person('jack',20,130)
# p1.eat()
# p1.run()
# Person.run()
# print(p1.weight,p2.weight)

'''
面向对象设计：
    1- 找出有什么对象(类)
        1- 老虎
            属性：
                体重---实例
                叫声---类属性
            方法
                吃
                叫---
        2- 羊
        3- 房间
    2- 关系组网

'''
class Tiger:
    def __init__(self,inWeight=200):
        self.weight = inWeight
    #叫---实例方法
    def roar(self):
        print('老虎叫---wow!---体重减少5斤！')
        self.weight -= 5

    # 吃---实例方法
    def feed(self,food):
        #1- 喂食正确--增加体重
        if food == '肉':
            self.weight += 10
            print('喂食正确，体重增加10斤！')
        #2- 喂食错误--减少体重
        else:
            self.weight -= 10
            print('喂食错误，体重减少10斤！')

class Room:
    def __init__(self,inNum,inAnimal):#编号与动物
        self.num = inNum
        self.animal = inAnimal

class Sheep:
    pass


t1 = Tiger()
# print(t1.weight)
# t1.roar()
# t1.feed('草')
# print(t1.weight)

# r1 = Room(2,t1)
#
# #房间实例.动物属性.叫操作
# r1.animal.roar()

#随机操作
from random import randint
# print(randint(0,2))#双闭0 1 2
#--------------------------游戏初始化操作-----------------
roomList = []#每一个元素是房间实例
for one in range(1,11):# 1- 10
    if randint(0,1) == 1:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(one,ani)
    roomList.append(room)

#-------------------------------------------------------

#时间操作
import time
startTime = time.time()#返回是单位是 s

while True:
    curTime = time.time()
    if curTime - startTime > 120:
        break

    #游戏逻辑


'''
继承：
    1- 如果子类没有 __init__方法，会自动调用父类的__init__
    2- 在父类的实例属性不够用的时候，子类自己有__init__方法，不会自动调用，就意味不会继承！
        如果话需要继承，手动调用

方法重写：是多态一种体现
    一个方法在父类和子类有不同的操作
    什么时候使用重写：父类有一个方法a  ,但是子类去继承，发现a方法不满足子类，
    为了保持整体一个模式，会重写这个方法，适合子类
'''
# author：xintian   time:2020-04-12
class VipCustomer:#VIP
    #
    welfare = '商品8折优惠+生日礼券'
    def __init__(self,inName,inAge):
        self.name = inName
        self.age = inAge

    def shopping(self):
        print('-----<VIP用户***江浙沪包邮>-----')


#业务扩展---需要升级SVIP-----但是要保证VIP权限
class SvipCustomer(VipCustomer):
    #
    svipWelfare = '金融理财+白条支付'

    def __init__(self,inName,inAge,inLevel):
        VipCustomer.__init__(self,inName,inAge)
        self.level = inLevel

    def shopping(self):
        print('-----<江浙沪包邮+福利礼品>-----')


#--------1.选择登陆级别----------
userLevel = input('VIP用户请求输入: 1 ;SVIP用户请求输入: 2:')
if userLevel == '1':
    name,age = input('---<VIP用户欢迎登录>----，请求输入：用户名,年龄').split(',')
    vip1 = VipCustomer(name,int(age.strip()))
    vip1.shopping()

elif userLevel == '2':
    name,age,level= input('---<SVIP用户欢迎登录>----，请求输入：用户名,年龄,等级').split(',')
    svip1 = SvipCustomer(name,int(age.strip()),int(level.strip()))
    for one in range(0,4):# 0 1  2 3
        if one > 2:#3
            print('SVIP只要3次购物超级福利机会，已使用完毕')
            super(SvipCustomer,svip1).shopping()#使用父类的 shopping()
            #需要调用父类的被重写方法：
            # super(子类类名，子类的实例名).方法（）
        else:
            svip1.shopping()#子类的shopping()

else:
    print('-----<抱歉暂时没有这个权限用户>-----')


# ===================对象继承====================================================

# class Tiger:
#     def roar(self):
#         print('父类-Tiger-的实例方法')
#
#     @staticmethod
#     def tell():
#         print('父类Tiger-的静态方法')
#
# class Sheep:
#     def roar(self):
#         print('父类-Sheep-的实例方法')
#
#     @staticmethod
#     def tell():
#         print('父类-Sheep-的静态方法')
#
# class SouTiger(Tiger,Sheep):
#     def roar(self):
#         print('子类的实例方法')
#
#     @staticmethod
#     def tell():
#         print('子类的静态方法')
#
# s1 = SouTiger()#创建子类、
# #1- 直接使用，就直接调用子类自己的方法
# s1.roar()
# #调用父类的实例方法---第一个父类优先
# super(SouTiger,s1).roar()
# #调用父类的静态方法---第一个父类优先
# super(SouTiger,s1).tell()
#
# super(Tiger,s1).tell()
#
# #那么我们要调用第2个父类的方法---super(你要调用的那个父类的前一个父类-类名,s1).roar()
# #1- 调用第2个父类的实例方法
# super(Tiger,s1).roar()
# #2-调用第2个父类的静态方法
# super(Tiger,s1).tell()


# 普通用户---父类--查看个人信息操作
# 自动化学员---子类---重写
#
# 好处：用户对象.查看数据()

