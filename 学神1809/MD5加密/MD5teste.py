#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# file:MD5teste
# datetime:2019/4/16 21:59
# software:PyCharm Community Edition
import  hashlib

md5 = hashlib.md5()
md5.update('123456'.encode())
password = md5.hexdigest()
print(password)