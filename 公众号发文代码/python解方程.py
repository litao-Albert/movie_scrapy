from sympy import *
import math

x=Symbol("x")
y=Symbol("y")

# 一元一次方程
res = solve([2*x+8-9],[x])
print("一元一次方程的解",res)

# 二元一次方程
res = solve([x+y-3,2*x+3*y-12],[x,y])
print("一元一次方程的解",res)

# 指数函数
res = solve([exp(x)-math.e],[x])
print(res)

# 对数函数
res = solve([log(8,2)-x],[x])
print(res)
