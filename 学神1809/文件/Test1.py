#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/16 12:08
# software:PyCharm Community Edition
import time
class Book(object):

    def Read(self,path,line=3):

        with open(path,'r',encoding='utf-8') as f:
            f.seek(0,2)    #    从起始位置到末尾
            end = f.tell()   #  得到指针现在得位置
            f.seek(0,0)   #  最起始得位置
            auto = str(input("是否开启自动：（y/n）?"))
            if auto == 'y':
                while True:
                    for i in range(line):
                        print(f.readline())
                    time.sleep(2)
                    if f.tell() == end:
                        break
            elif auto =='n':
                f.seek(0,2)
                end = f.tell()
                f.seek(0,0)
                while True:
                    if auto == 'n':
                        for i in range(line):
                            print(f.readline())
                    else:
                        print('头贴是不')
                    if f.tell() == end:
                        break
                    con = input('>>>>')
            else:
                print("你偷铁是不")
b = Book()
b.Read("C:\\Users\\黎涛\Desktop\\1.txt")

