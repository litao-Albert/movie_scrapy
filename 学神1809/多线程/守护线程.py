#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/23 13:48
# software:PyCharm Community Edition

'''
当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行流的最小单元，当设置多线程时，主线程会创建多个子线程，在python中，
主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。
15.3.1  threading介绍
1、threading是对thread模块的再封装，线程并发运行并且共享内存；
2、threading模块支持守护线程；
3、守护线程：
	     守护线程会在"该进程内所有非守护线程全部都运行完毕后,守护线程才会挂掉"。并不是主线程运行完毕后守护线程挂掉。
    守护线程守护的是：当前进程内所有的子线程
    主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，
        进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。
'''
import threading
import time
def say(name):
    print('1111 start time:%s'%time.ctime())
    print('hello %s'%name)
    time.sleep(4)
    print('func say stop  time%s'%time.ctime())
def hello(name):
    print('2222 start time:%s'%time.ctime())
    print('hello %s'%name)
    time.sleep(3)
    print('func hello stop time %s'%time.ctime())
print('___主线程开始___')

t1 = threading.Thread(target=say,args=('for',))
t2= threading.Thread(target=hello,args=('while',))
t1.setDaemon(True)
t1.start()
t2.start()
print('————主线程结束————')