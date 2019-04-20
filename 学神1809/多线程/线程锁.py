#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/23 14:08
# software:PyCharm Community Edition

'''
线程锁是为了保证共享数据的一致性，线程锁的意义在与同一个时间内，多个线程同时修改共享数据，果不加锁的话，会造成数据的不一致，
当我们加上锁以后，保证在同一个时间里，只能运行一个线程修改共享数据，其他线程阻塞等待该线程的结束。
结束后一定要释放锁，不然会一直阻塞下去。
'''
import threading,time
lock = threading.Lock() #加一个锁
class MyThread(threading.Thread):
    def run(self):
        lock.acquire()  # 声明全局
        global num
        time.sleep(1)
        num+=1
        msg = self.name + 'set num is' +str(num)
        print(msg)
        lock.release()  #释放锁
num = 0
def test():
    for i in range(5):
        t = MyThread()
        t.start()
        # t.join()  加join 阻塞是一样得
if __name__ == '__main__':
    test()