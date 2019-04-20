import time,threading
# class info:
#     def count(self):
#         f=open('D:\\text.txt','a')
#         sd=time.time()
#         print('打开用的时间:%s'%(sd))
#         for i in range(1000):
#             c=f.write('欢迎来到蜗牛学院学习')
#             sf=time.time()
#         f.close()
#         print('总共的时间:%s'%(sf-sd))
class Dome:
    def write_content(self):
        f=open(r'D:\\f.txt','a') #打开一个TXT文档
        start=time.time()  #计算打开这个文档的时间
        for i in range(100):
            f.write('欢迎来到蜗牛学院学习') #在这文档中写入100遍欢迎来到蜗牛学院学习
            end=time.time() #计算写入100次所花的时间
        f.close() #关闭文档
        print(end-start) #打印打开与写入的时间差
    for i in range(10):
        t=threading.Thread(target=write_content,args=())
        t.start()
Dome().write_content()



