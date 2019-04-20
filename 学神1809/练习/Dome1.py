# for i in range(3):
#     print(i)
#     for j in "abc":
#         print(j)
# a =  0
# while a < 10:
#     a += 1
#     print(a)
# for i in range(5):
#     if i == 2:
#        continue
#     print(i)
# outlist = {v:k for k,v in enumerate("avgdsdsadsd")}
# print(outlist)
import random
with open("D:\\a.txt",encoding='utf-8') as f:
    lines = f.readlines()
    name = random.choice(lines)
    # names = name.decode().replace('\n','')
    print(lines)
    print(name)
