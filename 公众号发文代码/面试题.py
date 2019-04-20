# 获取两个列表的交集、并集、差集
# a = [1,2,3,4]
# b = [4,3,5,6]
# jj1=[i for i in a if i in b] # 在a中的i，并且在也b中，就是交集
# jj2=list(set(a).intersection(set(b)))

# bj1=list(set(a).union(set(b))) # 用union方法

# cj1= list(set(b).difference(set(a))) # b中有而a中没有的      非常高效！
# cj2= list(set(a).difference(set(b))) # a中有而b中没有的      非常高效！
# print("交集",jj1)
# print("交集",jj2)

# print("并集",bj1)
# # print("并集",bj2)
# print("差集",cj1)
# print("差集",cj2)

# 1-100随机数
# import random
# res1=100*random.random()
# res2=random.choice(range(0,101))
# res3=random.randint(1,100)
# print(res1)
# print(res2)
# print(res3)
# 
#
# lambda好处
# a = ["苏州","中国","哈哈","","","日本","","","德国"]
# res=list(map(lambda x:"填充值" if x=="" else x,a))
# print(res)
# 
# 
# import jieba
# import pandas as pd
# pd.set_option('max_colwidth', 200)
# pd.set_option('display.max_rows',None)
# a = ["今天下雨,我骑车差点摔倒,好在我一把把把把住了！",
# "来到杨过曾经生活的地方,小龙女动情地说,我也想过过过儿过过的生活" ,
# "多亏跑了两步,差点没上上上海的车",
# "用毒毒毒蛇毒蛇会不会被毒毒死",
# "校长说:校服上除了校徽别别别的,让你们别别别的别别别的你非得别别的！"]
# res=[list(jieba.cut(i)) for i in a]
# print(res)
# ret=[" ".join(i) for i in res]
# print(ret)
# print(pd.DataFrame(ret))
# 
# import pandas as pd
# df=pd.read_excel("333.xlsx")
# print(df)

# import re
# s = "小明年龄18岁 工资10000"
# res=re.search(r"\d+",s).group()
# print("search结果",res)

# res=re.findall(r"\d+",s)
# print("findall结果",res)

# res=re.match("小明",s).group()
# print("match结果",res)

# res=re.match(r"\d+",s)
# print("试错，不加group为none,匹配不到",res)

# res=re.match("工资",s).group()
# print("match结果",res)




import time
class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name

    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)

cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print(id(cat),id(cat2),id(cat3))
print("---马上 删除cat对象")
del cat

print(id(cat2),id(cat3))
print("---马上 删除cat2对象")
del cat2

print(id(cat3))
print("---马上 删除cat3对象")
del cat3



