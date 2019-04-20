#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/30 10:35
# software:PyCharm Community Edition
import  base64

# s = 'my name is litao'
# # 加密
# result = base64.b64encode(s.encode())
# print(result)
# print('--------------------')
# result_str = str(result,'utf-8')
# print(result_str)
# #解密
# res = base64.b64decode(result)
# print(res)

with open('E:\\Download\\图片\\001.jpg','rb') as f:
    date = f.read()
    print(date)
    result = base64.b64encode(date)
    print(result)