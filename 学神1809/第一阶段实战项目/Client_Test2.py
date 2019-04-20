#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/24 22:26
# software:PyCharm Community Edition
'''
利用socket tcp和线程知识服务端分别将随机30个数字，发送给三个客户端。
   	然后分别需要计算
    1、这30个数字的 奇偶性 奇数返回True 偶数返回False
    2、这30个数字的 2倍
    3、这30个数字的 是否大于10
    要求用socket分布式部署给三个client来计算
将结果返回给服务端进行数据汇总显示.
'''
import socket
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',15070))
def double(date):
    date *=2
    return date
while True:
    # sock.send(b'hello I am client002')
    time.sleep(1)
    recv = sock.recv(1024).decode()
    if str(recv).isdigit():
        print("从服务器接收得数据是%s"%str(recv))
        date = double(int(str(recv)))
        date2 = '%s 得2倍是%s'%(recv,date)
        sock.send('hell I am client002\n'.encode())
        sock.send(str(date2+'\n').encode())
    else:
        print(recv)

sock.close()