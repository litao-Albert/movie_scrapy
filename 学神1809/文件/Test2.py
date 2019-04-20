#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/16 13:56
# software:PyCharm Community Edition

import os
m_name = os.getcwd()

# class File(object):
#     def __init__(self,path):
#         self.path = path
#
#     def Dir_name(self):
#         return os.listdir()
#     def re_name(self,new_name):
#         m_name = os.listdir(self.path)
#         for temp in m_name:
#             print(temp)
#             return os.rename(temp,new_name)
#
#
# f = File('C:\\Users\\黎涛\PycharmProjects\\untitled\\学神1809\\文件')
# list1=f.Dir_name()
# print(list1)
# list2 =f.re_name('Test1.py')
# print(list1)

for root,dirs,files in os.walk(m_name):
    for filename in files:
        print(os.path.join(root,filename))


