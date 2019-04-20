#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/23 13:57
# software:PyCharm Community Edition

'''
分析：join阻塞了主线程，前面主线程结束后，继续执行子线程，而我们加入join后，就会在主线程中等待子线程全部执行完毕，才能正常运行。
'''
import threading
import time
def run(number):
    print('%s.......start'%number)
    time.sleep(2)
    print('---------')
if __name__ == '__main__':
    print('—主线程开始--',threading.current_thread().name)
    thread_list = []
    for i in range(1,5):
        t = threading.Thread(target=run,args=(i,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
        t.join()
    print('--主线程结束---',threading.current_thread().name)