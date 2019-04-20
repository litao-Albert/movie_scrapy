# 实现n的阶乘

# n = int(input("请输入一个数字："))
# result = 1
# i =1
# while i<=n:
#     result = result*i
#     i+=1
# print(result)

# def test(n):
#     if n==1:
#         return 1
#     else:
#         return n*test(n-1)
# while True:
#     n = int(input("请你输入一个数字"))
#     print(test(n))

# n = int(input("请输入一个数字："))
# a,b = 0,1
# c = []
# while n>0:
#     c.append(b)
#     a,b = b,a+b
#     n-=1
# print(c)

def feibo(n):
    if n <= 1:
        return n
    elif n ==2:
        return 1
    return (feibo(n-1)+feibo(n-2))
n = int(input('>>>'))
a = [feibo(i) for i in range(1,n+1)]
print(a)