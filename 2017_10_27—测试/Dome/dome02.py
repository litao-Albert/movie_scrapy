import  socket
s=socket.socket()
s.connect(('127.0.0.1',9999))
while 1:
    date=input('请输入：')
    s.send(date.encode('gbk'))
    print(s.recv(1024).decode('gbk'))