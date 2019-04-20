from itertools import  count

# 程序 电脑的状态，优质的代码

# 手机号做密码
phone_pass = count(15200000000)

for var in phone_pass:
    if var ==15200000678:
        break
    print(var)
print("*"*100)
class Myiter:
    def __init__(self): # 直接是一个迭代器
        self.num = 15200000000
    def __iter__(self):
        return self
    def __next__(self):
        self.num +=1
        if self.num == 15200001000:
            raise  StopIteration
        return  self.num
a = Myiter()
for var in a: # 自动捕获StopIteration
    print(var)