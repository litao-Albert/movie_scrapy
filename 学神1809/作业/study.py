#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/19 10:20
# software:PyCharm Community Edition
#1. 编程实现对一个元素全为数字的列表，求最大值、最小值

# 1.编程实现对一个元素全为数字的列表，求最大值、最小值
class Dister(object):
    def __init__(self,list1):
        self.list1=list1
    def Max(self):
        max = self.list1[0]
        for i in self.list1:
            if max<i:
                max = i
        print(max)
    def min(self):
        min = self.list1[0]
        min = self.list1[0]
        for i in self.list1:
            if min>i:
                min = i
        print(min)
D = Dister([123,45,66,78,90])
D.Max()
# D.min()
'''
2. 编写程序，完成以下要求：
提示：统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
利用 字典和count 还有遍历
'''
def str_Count():
    str = "hell world"
    new_list = list(str)
    dict = {}
    for i in new_list:
        dict[i]=new_list.count(i)
    print(dict)
if __name__ == '__main__':
    str_Count()
'''
3. 编写程序，完成以下要求：
完成一个路径的组装
先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/abc/efg
提示：字符串的拼接
'''
import os
frist = input('请输入第一个路径：')
second= input('请输入第二个路径：')
three= input('请输入第三给路径：')
last = os.path.join(frist,second,three)
print(last)
'''
4. 编写程序，完成“学生管理器”项目
需要完成的基本功能：
a.添加学生
b.删除学生
c.修改学生
d.查询学生
e.退出系统
程序运行后，除非选择退出系统，否则重复执行功能
1. 编程实现 9*9乘法表
提示：使用循环嵌套
2.用函数实现求100-200里面所有的素数
提示：素数的特征是除了1和其本身能被整除，其它数都不能被整除的数
for+if
3.请用函数实现一个判断用户输入的年份是否是闰年的程序
提示： 1.能被400整除的年份 2.能被4整除，但是不能被100整除的年份 以上2种方法满足一种即为闰年
'''
import sys
class Student(object):
   def __init__(self):
       self.dict_student = {
           'name':[],
       }
   def add(self):
       while True:
           stu_name = input('请输入学生得姓名：')
           if stu_name != 'exit':
               self.dict_student.get('name').append(stu_name)
           else:
               break
           print(self.dict_student)
   def del_stu(self):
       while True:
           stu_name = input("请输入要删除得学生姓名：")
           if stu_name != 'exit':
               self.dict_student.get('name').remove(stu_name)
   def select(self):
       stu_name = input('请输入要查询学生得姓名：')
       self.dict_student.get('name').find(stu_name)
   def doquit(self):
       self.sys.quit()

if __name__ == '__main__':
    s = Student()
    print('---------欢迎使用蜗学生管理系统------------------')
    print('---------请选择你的选选项 a.添加学生,b.删除学生c.修改学生d.查询学生e.退出系统')
    print('-------------------------------------------------')
    stu = str(input('请输入选项：'))
    if stu == 'a':
        s.add()
    elif stu == 'b':
        s.del_stu()
    elif stu == 'd':
        s.select()
    elif stu == 'e':
        s.doquit()

    else:
        print('你输入错误，拜拜')


for i in range(1,10):
    for j in range(1,i+1):
         print("%s * %s =%s\t"%(j,i,i*j),end='')
    print('')

def num(start,end):
    new_list = []
    for i in range(start,end+1):
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            new_list.append(i)
    print(new_list)
num(1,200)
def day():
    year = int(input("请输入年："))
    if(year % 4) == 0 and (year % 100)!=0 or(year % 400) == 0:
        print('{0}瑞年'.format(year))
    else:
        print('{0}不是瑞年'.format(year))
day()





'''
5. 使用if，编写程序，实现以下功能：
从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
'''
user = 'admin'
pwd = '123456'
count = 0
while count<3:
    name = str(input('请输入用户名：'))
    password = str(input('请输入密码：'))
    if name == user and password == pwd:
        print("欢迎进入LOL的世界")
        break
    else:
        print("你输入得用户名或者密码错误")
        count+=1
        print("你还有%s次机会"%(3-count))
'''
7.在 Python 中,类和对象有什么区别?对象如何访问类的方法? 创建一个对象时做了什么?
'''

'''
8.请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3], [4,5,6]....]
提示：利用截取
'''

'''
9.请写出一段 Python 代码实现删除一个 list 里面的重复元素
集合，if判断，for
'''
list1 = [1,1,45,67,8,9,6,9,6,45,67,34,56,56,78,67,89,110]
list2 = set(list1)
list3 =list(list2)
print(list3)

'''
10.写出一个函数,给定参数 n,生成含有 n 个元素值为 1~n 的数 组,元素顺序随机,但值不重复
提示：random
'''
import random
def num_test(n):
    list1 = []
    i=0
    while i<n:
        list1.append(random.randint(1,n))
        i+=1
    print(list1)
if __name__ == '__main__':
    num_test(200)


'''
12.在不用其他变量的情况下，交换a、b变量的值
提示：赋值
'''
a = 200
b = 300
print("交换之前得a是%d"%a)
print("交换之前得b是%d"%b)
print("-----------------------------------------")
a = a+b
b = a-b
a =a-b
print("交换之后得a是%d"%a)
print("交换之后得b是%d"%b)


'''
13.如何在一个 function 里设置一个全局变量
提示：不用提示
'''
total=0
def sum (arg1,arg2):
    total=arg1+arg2
    print('函数内是局部变量',total)
    return total
sum(10,20)
print('函数外是全局变量',total)

'''
14.用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
20160818 是今年第x天
'''
import  datetime
def just_day():
    y = input('请输入年：')
    m= input('请输入月：')
    d = input('请输入日：')
    # 把年月日标准化
    datayear = datetime.date(y,m,d)
    l = datayear.year # 得到输入得年
    lastDate = datetime.date(l-1,12,31) #得到上一年得最后一天
    dayCount = datayear-lastDate #减去上一年得最后一天就得到今年得第几天
    print('%s是%s年的第%s天' % (datayear, y, dayCount.days))




'''
15. 编写“学生管理系统”，要求如下：
必须使用自定义函数，完成对程序的模块化 学生信息至少包含：姓名、年龄、学号，除此以外可以适当添加 必须完成的功能：
添加、删除、修改、查询、退出
'''

'''
3.根据以下信息提示，请帮小明计算，他每月乘坐地铁支出的总费用
1.提示信息:
北京公交地铁新票价确定
据北京市发改委网站消息称，北京市将从2015年12月28起实施公共交通新票价：地铁6公里(含)内3元，公交车10公里(含)内2元，使用市政交通一卡通刷卡乘公交车普通卡5折，学生卡2.5折。
　　具体实施方案如下：
　　一、城市公共电汽车价格调整为：10公里(含)内2元，10公里以上部分每增加1元可乘坐5公里。使用市政交通一卡通刷卡乘坐城市公共电汽车，市域内路段给予普通卡5折，学生卡2.5折优惠;市域外路段维持现行折扣优惠不变。享受公交政策的郊区客运价格，由各区、县政府按照城市公共电汽车价格制定。
　　二、轨道交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，每增加1元可乘坐20公里。使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。
要求：
假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁；每月月初小明第一次刷公交卡时，扣款5元；编写程序，帮小明完成每月乘坐地铁需要的总费用
'''



