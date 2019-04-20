#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/19 16:23
# software:PyCharm Community Edition
# dict = {
# }
# s = 'hellddhhhhho word'
# h= 0
# for i in s:
#   if i == 'h':
#       h+=1
# print(h)
# list= [1,2,3,4,5,6]
# new_list = []
# new_list.append(list[0:3])
# new_list.append(list[3:6])
# print(new_list)

list1 = [1,2,3,4,52,323,4,51,3,1,2,3]
for i in range(len(list1)-1):
    if list1[i]<=list1[i+1]:
        list1[i]=list1[i+1]
        list1.pop()
print(list1)