import socket
class client:
    def __init__(self):
        self.c=socket.socket()#生意客户端的一个套接字对象
        self.c.connect(('127.0.0.1',9999)) #通过套接字对象向目标服务器发起连接请求
    def re_sd(self):
        print(self.c.recv(1024).decode())
        name=input('昵称:')
        self.c.send(name.encode())
        while 1:
            i=input('请输入：')#准备向服务器发送消息
            self.c.send(i.encode())#通过套接字对象向服务器发送经转码后得消息
            print(self.c.recv(1024).decode())#接送服务器发来的消息

client().re_sd()