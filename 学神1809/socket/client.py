import  socket
# 创建套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口
sock.connect(('127.0.0.1',9000))
while True:
    send = str(input("客户端:"))
    sock.send("客户端:",send.encode())

    print("服务端：",sock.recv(1024).decode())