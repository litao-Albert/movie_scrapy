#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/23 13:24
# software:PyCharm Community Edition
import time
import threading
def say(name):
    print('1111 start time:%s'%time.ctime())
    print('hello %s'%name)
    time.sleep(3)
    print('func say stop  time%s'%time.ctime())
def hello(name):
    print('2222 start time:%s'%time.ctime())
    print('hello %s'%name)
    time.sleep(2)
    print('func hello stop time %s'%time.ctime())
def main():
    print('我是main')


print('___主线程开始___',threading.current_thread().name)
t1 = threading.Thread(target=say,args=('for',))
t2 = threading.Thread(target=hello,args=('while',))
t3 = threading.Thread(target=main,args=())
t1.setName('风一般得男子')
t1.start()
print(t1.getName())
t2.start()
t3.start()
print('__住线程结束__',threading.current_thread().name)
# say('for')
# hello('while')
