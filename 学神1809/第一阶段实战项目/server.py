#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/24 17:01
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
import threading
import time
import socket
import random


def setResponse(sock,address):
    rand_list = [random.randint(1, 30) for i in range(30)]
    print("%s:%s is connect"%address)
    while True:
        #接收客户端发来得消息
        for i in rand_list:
            sock.send(str(i).encode())
            recv = sock.recv(1024).decode()
            print(recv)
            # sock.send(b'hello %s:%d i I am server'%(address[0].encode(),address[1]))
            time.sleep(1)


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',15070))
sock.listen(5)
while True:
    try:
      client,address = sock.accept()
      t = threading.Thread(target=setResponse,args=(client,address))
      t.start()
    except Exception as e:
        print(e)
sock.close()

