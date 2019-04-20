import socket
s=socket.socket() #生成一个服务器的套接字对象
s.bind(('127.0.0.1',9999))#在局域网内公布服务器自己的ip和端口
s.listen(5)#开启监听序列
while 1:
    con,addr=s.accept() #建立和客户端的连接，并返回客户端的连接对象和客户端的ip及端口号
    while 1:
        redate=con.recv(1024).decode('gbk') #通过客户端连接对象接收从当前客户端发过来的消息并转码
        print(addr,':',redate)
        con.send(redate)