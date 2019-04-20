# def in_fo(a):
#     if type(a)==int:
#         print(a+1)
#     if  type(a)==str:
#        print(a+'1')
#     if type(a)==list:
#         a.append(1)
#         return a
#
# print(in_fo([1,2]))
# total=0
# def sum (arg1,arg2):
#     total=arg1+arg2
#     print('函数内是局部变量',total)
#     return total
# #globals(total)
# sum(10,20)
# print('函数外是全局变量',total)
#while True:
# li=[]
# def appe_sdsd(a):
#    li.append(a)
# def in_fo():
#  while True:
#    c=input('输入:')
#    if c!='quit':
#     appe_sdsd(c)
#     print(li)
#    else:
#      break
#  print(li)
# in_fo()
# func=lambda x:x*2
# print(func(3))
# fff=lambda x,y,z:x*y+z
# print(fff(3,4,5))

# def fun():
#     """This is a document information
#     Please see it."""
#     print('document test')
#     return
# print(fun.__doc__)
# func=lambda x,y:x**y
# print(func(3,4))

# def in_fo(a):
#     a.sort()
#     return a
# print(in_fo([2,3,56,43,67]))
def count(string,substr):
    l=len(substr)
    sum=0
    for i in range(len(string)):
        if string[i:i+1]==substr:
            sum+=1
    return sum
s="""mkijjsdsddzxjfidjfdfddfdfdf
   sdsdsdsdsddsddsdsg"""
print(count(s,"s"))


