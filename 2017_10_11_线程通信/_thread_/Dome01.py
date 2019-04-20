
# def loop():
#     print('thread %s is runing...'%(threading.current_thread().name))
#     for i in range(5):
#         print('thread %s >>>%s'%(threading.current_thread().name,i))
        # print('thread %s is runing...'%threading.current_thread().name)
        # t=threading.Thread(target=loop)
        # t.start()
        # t.join()
# loop()
from  threading import Thread
from time import ctime,sleep
class Deom:
    def music(self,music):
        for i in range(3):
            print('I was listening to %s,%s'%(music,ctime()))
            sleep(1)
    def movie(self,movie):
        for i in range(3):
            print('I was at %s!%s'%(movie,ctime()))
            sleep(5)
# 单线程
# if __name__=='__main__':
#     d=Deom()
#     d.music('演员')
#     d.movie('战狼2')
#     print('all over %s'%ctime())
#多线程
if __name__=='__main__':
    threads=[]#定义一个数组用来转线程
    d=Deom()
    t1=Thread(target=d.movie,args=('魔兽世界',))
    threads.append(t1) #把创建好的线程t1装进数组中
    t2=Thread(target=d.music,args=('成都',))
    threads.append(t2)#把创建好的线程t2装进数组中
    for i in range(len(threads)): #遍历数组（数组装载了t1和t2两个线程）
        threads[i].setDaemon(True)#声明为守护线程，必须在start方法之前调用
        threads[i].start() #开始线程活动
    threads[i].join()#用于等待线程终止 作用：在子线程完成之前，这个子线程的父线程将一直被阻塞
    print('all over %s'%ctime())



