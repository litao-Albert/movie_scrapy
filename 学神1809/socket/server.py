import  socket

def setResponse(sock,addr):
    while True:
        # 接收客户端发来的信息
        recv = sock.recv(1024).decode()
        print(recv)
        send = input("客户端：")
        sock.send(send.encode())


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',9000))
    sock.listen(5)
    while True:
        client,address = sock.accept()
        setResponse(client,address)