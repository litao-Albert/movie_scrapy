# 1.有一对兔子从出生后3月起一个月生一对小兔子，小兔子长到
# 第三个月后每个月又生一对兔子，假如兔子都不死，问每个月
# 的兔子总数是多少
# class Rb:
#     month=1
#     def group(self): #兔子的年龄，每调用一次
#         self.month+=1
#     def bir(self,a):#每调用一次就让当前这对兔子生小兔子
#         a.append(Rb())
# class count():
#     list=[Rb()] #生成一个笼子，并放入一对兔子
#     def add_num(self):
#         for i in range(1,13):
#             for j in self.list:
#                 if j==None:
#                     self.list.append(Rb())
#                 else:
#                     if j.month<3:
#                         j.group()
#                     else:
#                         j.bir(self.list)
#             print(i,'月',len(self.list))
# count().add_num()
# 2.写成了一个游戏机器人自动游戏比赛，说明：先定义一个基类：
# AutoPeople，类中存在一个全局类成员，所有队员有效
# GameDic = ['石头','剪刀','布']含义为 石头>剪刀>布>石头 等
# 然后需要定义一个分数值 Score，完成两个机器人之间的比赛！
import random
class AutoPeople:
    GameDic={'石头':'剪刀','剪刀':'布','布':'石头'}
    def __init__(self):
        self.score=0
    def out(self):
        pass
class AutoPeople1(AutoPeople):
    def out(self):
        return self.GameDic.keys()[0]
class AutoPeople2(AutoPeople):
    def out(self):
        return self.GameDic.keys()[random.randint(0,2)]
class Dostrat:
    def __init__(self,pa,pb):
        self.pa=pa
        self.pb=pb


#  3.假设一个小球从20米高落下，然后在弹起，让后再落下，每
#  次跳起的高度为上一次的一半，那么，20次后小球运行了多少
# 米
class ball:
    def sum(self):
     s=30
     h=10
     for i in range(2,20):
      s=s+h+h/2
      h=h/2
     print(s)
ball().sum()

