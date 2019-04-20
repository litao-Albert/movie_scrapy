"""
闰年是公历中的名词。
普通年：能被4整除但不能被100整出的年份为普通瑞年
世纪年：能被400整除的为世纪闰年
"""
# year = int(input('输入年：'))
#
# if (year % 4) ==0 and (year % 100) !=0 or (year % 400) ==0:
#
#     print('{0}瑞年'.format(year))
# else:
#     print('{0}不是瑞年'.format(year))

#
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end = ' ')
#         j += 1
#     print('')
#     i += 1
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         if j <= i:
#             sum = j*i
#             print('%d*%d=%d\t'%(j,i,sum),end = ' ')
#     print(' ')
"""斐波拉基数列，该数列中有N个数字，该数列中，从第三个数字开始：数值 =前一个数字 +前面一个数字
"""

# def feibo(n):
#     a,b = 0,1
#     c = []
#     while n > 0:
#         c.append(b)
#         a,b = b,a+b
#         n-=1
#     print(c)
#
# feibo(9)

# 1、根据输入数字，如果是1-5，显示今天是工作日，否则是休息日
# while 1:
#     s = int(input("请输入一个数字："))
#     if 1<= s <=5:
#         print("今天是 工作日")
#     else:
#         print("今天是休息日")
# 通过嵌套for循环实现空心正方形的输出
# i = 1
# while i <= 5:
#     j = 5
#     while j >= i:
#         print("*",end = ' ')
#         j -= 1
#         continue
#     print('')
#     i += 1
# import copy
# a = [1,2,3,4,5,6,['a','b']]
#
# b = a  #赋值
# c =copy.copy(a)
#
# d = copy.deepcopy(a)
# a.append(7)
# a[6].append('c')
# print("浅拷贝：",c)
# print("深拷贝：",d)
# print("a的地址:",id(a))
# print("c的地址：",id(c))
# print("d的地址：",id(d))

# def fib():
#     a,b = 0,1
#     while True:
#         yield a,b
#         a,b = b ,a+b
# if __name__ == '__main__':
#     f = fib()
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
# it = iter([1,2,3,4,5,6])
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break
# 1-100的质数， 质数：质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
list1 = []
i = 2
for i in range(2,101):
    j = 2
    for j in range (2,i):
        if i%j == 0:
           break
    else:
        list1.append(i)
print(list1)






