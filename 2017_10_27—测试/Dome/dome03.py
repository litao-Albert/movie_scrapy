import socket
import time
for i in range(1,2):
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    mysocket.connect(('192.168.0.132',2425))
    packetID=str(time.time())
    name='administrator'
    host='localhost'
    command=str(0x00000020)
    content='this is the message from Python'
    for i in range(10):
        message='1.0:'+packetID+':'+name+':'+host+':'+content
        mysocket.send(message.encode('gbk'))
    mysocket.close()