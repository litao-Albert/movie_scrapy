'''
a=23
b=34
if a>b:
    print (a)
else:print(b)
'''
'''a=45
b=34
if a>b and b>20:
    print(a+b)
elif a<b or a<0:
    print(a-b)
else:print(a*b)
'''
'''s=str(input('请输入一个字符：'))
if s.isupper():
    print(s.lower())
elif s.islower():
    print(s.upper())
else:print(s)
'''
'''d=int(input('请输入年：'))
e=int(input('请输入月：'))
f=int(input('请输入日：'))
ly=False
if d%100==0:
    if d%400==0:
        ly=True  #是瑞年
    else:ly=False
elif d%4==0:
    ly=True #是瑞年
else:ly=False
if ly==True: #2月为瑞年
    ms=[31,29,31,30,31,30,31,31,30,31,30,31]
else:ms=[31,28,31,30,31,30,31,31,30,31,30,31]
days=0
for i in range(1,13):#从1到12判断，确定月份
    if i==e:
        for j in range(i-1):
            days+=ms[j]
            print(days+d)
            '''
class sum:
    def count(self):
        score={'语文':90,'数学':80,'英语':98}
        li=list(score.values())#获取健值 并转成列表
        m=max(li)
        for i in score:
            if score[i]==m:
                print(i)
sum().count()
# a=[1,2]
# b=[3,4]
# c=[a,b]
# print(c)



