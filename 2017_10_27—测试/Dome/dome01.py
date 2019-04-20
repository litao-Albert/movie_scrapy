import socket
s=socket.socket()
s.bind(('127.0.0.1',9999))
s.listen(5)
while 1:
    con,addr=s.accept()
    while 1:
        redate=con.recv(1024).decode('gbk')
        print(addr,':',redate)
        con.send(redate)