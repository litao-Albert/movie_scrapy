#coding:utf-8

import copy

a = [1,2,3,4,[5,6,7]]
b = a  # 把a赋值给b
# print('a的id:%s,b的id:%s'%(id(a),id(b)))
c = copy.copy(a)  # 把a拷贝给c  浅拷贝 没有拷贝子对象，所以原始数据改变，子对象会改变
print(c)
# print(id(c))
d = copy.deepcopy(a)    # 把a拷贝给d  深拷贝  包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
print(d)
print('*'*100)
a[4].append('a')
a.append(5)
print(a)
print(c)
print(d)