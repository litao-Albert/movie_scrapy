# def add (a,b):
#     return a+b
# print(add(34,45))

# def sum (n):
#     sum1=0
#     for i in range(1,n+1):
#         sum1=sum1+i
#         i=i+1
#     return sum1
# print(sum(100))
# def add(*a):
#     return sum(a)
# x=add(1,2)
# print(x)
# def info(i,k,j):
#     if k=="+":
#         return i+j
#     if k=='-':
#         return i-j
#     if k=='*':
#         return i*j
#     if k=='/':
#         return i/j
#
# print(info(1,"/",2))
#简单的计算器
# def info(a,b,c):
#     print(a+b)
# def info1(a,b,c):
#     print(a*b)
# def info2(a,b,c):
#     print(a-b)
# def info3(a,b,c):
#     print(a/b)
# a=float(input('a:'))
# c=input('符号:')
# b=float(input('b:'))
# if c=='+':
#     info(a,b,c)
# if c=='*':
#     info1(a,b,c)
# if c=='-':
#     info2(a,b,c)
# if c=='/':
#     info3(a,b,c)
    #实现count的方法
# s='kjjjsidjsidjsdsdsd'
# def count(string,str,begin=0,end=0):
#    # news=string[begin:end]
#     li=string.split(str)
#     print(len(li)-1)
# count(s,'j',0,len(s))
# def count(string,substr,begin=0,end=0):
#     newstr=string[begin:end]
#     sum=0
#     l=len(substr)
#     for i in range(len(newstr)):
#         if newstr[i:i+l]==substr:
#          sum+=1
#     return sum
# s='hhhkkomjijjm'
# print(count(s,'m',0,len(s)))
# def add (a,*b):
#     return a,b
# print(add(1,2,3,4,5))
list1=[2,3,8,4,9,5,7]
list2=[5,6,10,17,11,2]
list3=list1+list2
list3.sort()
s=set(list3)
s1=list(s)
print(s1)


