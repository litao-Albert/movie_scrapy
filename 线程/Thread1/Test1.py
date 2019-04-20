from threading import Thread
from multiprocessing import Queue

#t = Thread() #初始化实例化一个线程

import time
def work(l):
	print('开启线程...')
	l.append('a')
	print(l)
	print('结束线程...')

def main():
	l = [1,2,3] # 普通的列表
	t = Thread(target=work,args=(l,)) #这个线程工作work函数
	t1 = Thread(target=work,args=(l,))
	thread_list = [t,t1]
	for t in thread_list:
		t.start()
	for t in thread_list:
		t.join()

if __name__ == '__main__':
	main()

#GIL锁：Python编译环境Cpython: GIL
	#线程可以共享所有数据
	#如果线程是一个异步运行
		#a.b.c