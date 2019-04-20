import socket
c=socket.socket() #生成一个客户端的套接字对象
c.connect(('127.0.0.1',9999)) #通过这套接字对象向目标服务器发起连接请求
while 1:
    date=str(input('输入：') )#准备好向服务器发送的消息
    c.send(date.encode('gbk'))#通过套接字对象向服务器发送经gbk转码后的消息
    print(c.recv(1024).decode('gbk'))
