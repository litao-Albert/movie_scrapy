#coding:utf-8
import  socket

sock = socket.socket()
sock.bind(("127.0.0.1",56))
sock.listen(5)
while 1:
   client,addres = sock.accept()
   while 1:
     recv = client.recv(1024).decode()
     print(addres,":",recv)
     if recv == "exit":
         break
     else:
         data = input("输入：")
         client.send(data.encode('utf-8'))
