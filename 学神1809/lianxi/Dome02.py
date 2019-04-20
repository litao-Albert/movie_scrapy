# list=['a','b','c']
# print(id(list))
# print(id(list[0]))
# list[0]='e'
# print(id(list[0]))
# def change(val):
#     val=0
# num=1
# change(num)
# print(num)
# li=[]
# def jjj_ik(a):
#     li.append(a)
# def in_fo():
#  while True:
#      c=input("输入：")
#      if c!='quit':
#          jjj_ik(c)
#          print(li)
#      else:
#          break
# print(li)
# in_fo()
# def count(string,substr,begin=0,end=0):
#     newstr=string[begin:end]
#     li=newstr.split(substr)
#     print(len(li)-1)
# s='dsdsdsdsdddfff'
# count(s,"sd",0,len(s))
def count(string,substr,begin=0,end=0):
    newstr=string[begin:end]
    l=len(substr)
    sum=0
    for i in range(len(newstr)):
        if newstr[i:i+l]==substr:
            sum+=1
    return sum
s='midsjdsjdjsdsdd'
print(count(s,'ds',0,len(s)))
# class calcut:
#      def __init__(self,a,b):
#          self.a=a
#          self.b=b
#      def in_fo(self):
#        print(a+b)
#      def in_fo1(self):
#        print(a*b)
#      def in_fo2(self):
#        print(a-b)
#      def in_fo3(self):
#        print(a/b)
#      def inti(slef):
#          if c=='+':
#             slef.in_fo()
#          try:
#           if c=='/':
#             slef.in_fo3()
#          except Exception as e:
#              print(e)
#          if c=='*':
#             slef.in_fo1()
#          if c=='-':
#             slef.in_fo2()
# a=float(input('请输入a:'))
# c=input('请输入符号:')
# b=float(input('请输入b:'))
# dc=calcut(a,b)
# dc.inti()

# def in_fo(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#         i=i+1
#     return sum
# print(in_fo(100))