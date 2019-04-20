#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/17 12:42
# software:PyCharm Community Edition
import time
class File():

    def o_file(self,path):

        try:
            f = open(path,'r',encoding='utf-8')
            try:
                while True:
                    for i in range(3):
                        print(f.readline())

                    time.sleep(3)
                    content = f.readline()
                    if len(content) == 0:
                        break
            finally:
                f.close()
        except:
            print('没有这个文件')
f = File()
f.o_file('C:\\Users\\黎涛\Desktop\\1.txt')