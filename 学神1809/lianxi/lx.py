'''
r=float(input('请输入半径：'))
a=3.14
s=2*a*r
d=a*a*a
print('圆的周长：',s)
print('圆的面积：',d)
'''
'''
a=int(input('请输入数字a：'))
b=int(input('请输入数字b:'))
print((a-b)*(a+b))
print(a**b//b)
'''

score=[45,98,65,87,43,68,74,20,75,85,76,79,99]
a=[]
b=[]
c=[]
d=[]
e=[]
for i in score:
    if i>=90 and i<=100:
        a.append(i)
    elif  i>=80 and i<90:
        b.append(i)
    elif i>=70 and i<80:
        c.append(i)
    elif  i>=60 and i<70:
        d.append(i)
    else:
     e.append(i)
print ('A',a,'B',b,'C',c,'D',d,'E',e)












