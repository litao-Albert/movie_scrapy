#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/16 22:34
# software:PyCharm Community Edition

class MyException(Exception):
    def __init__(self,length,atleast):
        super().__init__()
        self.length = length
        self.atleast = atleast

try:
    nam = 10
    # open('1.txt','r',encoding='utf-8')
    print(nam)

except (FileNotFoundError,NameError) as e:
    print(e)
    print("错误%s"%FileNotFoundError)
    print('这是一个nameerror得错误%s'%NameError)
except :
    pass
else:
    print("没有报错")
finally:
    print('------finally----')
print('-----------------------------------------------------------------------------')
class Test(object):

    def start(self):

        try:
            num = input('请输入长度:')
            if len(num) < 3:

                raise MyException(len(num),3)
        except MyException as s:
            print('当前长度%s,最少的长度%s'%(s.length,s.atleast))
        else:
            print("没有报错")
T = Test()
T.start()