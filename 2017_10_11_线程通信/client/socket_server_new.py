import  socket
from threading import Thread
import time
import  datetime
import threading
class server:
    def __init__(self):
        self.s=socket.socket()#生成服务端的套接字对象
        self.s.bind(('127.0.0.1',9999)) #在局域网内公布服务器自己的ip和端口
        self.s.listen(5) #开启监听序列
    def server_ac(self):
        dict={}
        user=[]
        while 1:
          con,addr=self.s.accept() #建立与客户端的连接，并返回客户端的连接对象和客户端的ip以及端口号
          user.append(con)
          date= repr(dict)+'&'+'连接成功！请输入昵称：'
          con.send(date.encode())#向客服端发送消息并转码
          t=threading.Thread(target=self.thr_s_r,args=(con,addr,dict,user))
          t.start()
    def thr_s_r(self,con,addr,dict,user):
         name=con.recv(1024).decode()
         dict.update({addr:name})
         con.send((repr(dict)+"&"+'欢迎你'+name).encode())
         while 1:
            date=con.recv(1024).decode()#接收当前客户端发来的消息并转码
            print(dict.get(addr)+':'+date)
            con.send((dict.get(addr)+':'+date).encode())

            send_data = (repr(dict)+"&"+dict.get(addr)+' 于 '+datetime.datetime.now().strftime('%H:%M:%S')+':'+'\n'+date).encode()
            for i in user:
                i.send(send_data)


server().server_ac()
