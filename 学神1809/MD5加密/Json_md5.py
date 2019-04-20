#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/30 9:57
# software:PyCharm Community Edition
import json
import os
date_json = {
    "name":"xiaoming",
    "age":18,
    "addr":"重庆市"

}
j = json.dumps(date_json,ensure_ascii=False)
print(j)
print(type(j))
with open('date.json','a',encoding='utf-8') as  f:
    f.write(j+'\n')
with open('date.json','r',encoding='utf-8') as f:
    date = f.read()
    print(date)
#     print(type(date))
m = json.loads(j)
print('----------------------------------------')
print(m)
print(type(m))
# os.rmdir("1")