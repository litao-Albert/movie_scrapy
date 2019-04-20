#打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d=%d\t'%(j,i,j*i),end='')
#     print('\n')
# for i in range(0,10,3):
#     print(i)
#水仙花树
"""for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100)
    if a**3+b**3+c**3==i:
        print(i)
"""
#排序
li=[3,65,22,102,4]
# li.sort()
# print(li)
temp=0
for i in range(len(li)):
    for j in range(len(li)-1):
     if li[j]>li[j+1]:
        temp=li[j]
        li[j]=li[j+1]
        li[j+1]=temp
    print(li[i])

#猜字游戏
"""
import random
s=random.randrange(0,1000)  # 系统随机生成一个数
# print(s)
count=0
while True:
   count=count+1
   d=int(input('请输入一个数字：'))
   if d>s:
     print('大了')
   elif d<s:
     print('小了')
   else:
     print('正确通过')
     break
print('你一共输了：',count)
"""
#输入三个整数x，y,z，请把这三个数有大到小输出
# x=int(input('输入x:'))
# y=int(input('输入y:'))
# z=int(input('输入z:'))
# li=[]
# li.append(x)
# li.append(y)
# li.append(z)
# li.sort()
# print(li)

#一个10000以内的整数，它加上100和加上268都是一个完全平方数，请问该数是多少
"""
import math
for i in range(1,10000):
    a=i+100
    b=i+268
    s=int(math.sqrt(a))
    l=int(math.sqrt(b))
    if s*s==a and l*l==b:
        print(i)
"""
# import math
# s = 16
# l = int(math.sqrt(s))
# print(l)


#打印一个直角三角形
"""for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='\t')
    print()
"""
# li=[3,65,22,102,4]
# li1=[]
# for i in range(len(li)):
#     m=min(li)
#     li1.append(m)
#     li.remove(m)
# print(li1)
#打印*号金字塔
# def in_fo(a):
#     for i in range(1,a+1):
#        print(' '*(a-(i-1))+'*'*(2*i-1))
# in_fo(4)
#
# li=[66,11,88,22,33,44,55,77,99,90]
# li1=[]
# li2=[]
# for i in li :
#     if i >=66:
#         li1.append(i)
#     else:
#         li2.append(i)
# dict={'key1':0,'key2':0}
# dict['key1']=li1
# dict['key2']=li2
# print (dict)