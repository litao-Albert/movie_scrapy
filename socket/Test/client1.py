#coding="utf-8"
import  socket

sock = socket.socket()

sock.connect(("127.0.0.1",56))
while 1:
    date = input('输入：')
    sock.send(date.encode('utf-8'))
    print(sock.recv(1024).decode('utf-8'))
