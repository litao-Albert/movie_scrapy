for i in range(1,1000):
      s = 0
      for j in range(1,i-1):
           if i%j == 0:
                s = s+j
                if s == i:
                    print(i)
import math
for i in range(2, 1000):
    factors = []  #因子列表，i 每次循环都清空
    for j in range(1, math.floor(i/2)+1):
        if i%j == 0:
            factors.append(j)
    if sum(factors) == i:
        print(i, end=',')
