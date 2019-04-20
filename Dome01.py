from PyQt5 import QtGui
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import socket
import threading ,time

# help(QLineEdit)
class Login(QWidget):
    def __init__(self):
        QtGui,QWidget.__init__(self)  #初始化组件
        self.setGeometry(500, 300, 600, 500)  #指定窗体位置和大小
        self.setWindowTitle("chat")  #窗体设置标题
        palette=QtGui.QPalette()
        icon=QtGui.QPixmap('C:\\Users\\Administrator\\Desktop\\white-cloud.jpg')
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon)) #添加背景图片
        self.setPalette(palette)
        self.c=socket.socket()
        self.c.connect(('127.0.0.1',9999))
        self.addUI()
        self.show()
        threading.Thread(target=self.push_send).start()
        threading.Thread(target=self.show_msg).start()
    def addUI(self):   #添加各种组件
        # grid = QGridLayout()
        # grid.setSpacing(10)
        # labe = QLabel('XXXX管理系统',self)
        # labe.setGeometry(120,30,200,40)
        # labe.setFont(QFont('微软雅黑',18,QFont.Bold))
        #labe.setText("<font color=%s>%s</font>" %("gred",'XXXX管理系统'))  设置字体颜色
        # lab1 = QLabel(self)
        # lab1.setFont(QFont('微软雅黑',10,QFont.Bold))
        # lab1.setGeometry(60,100,60,30)
        #聊天内容
        text =QTextEdit(self)
        text.setPlaceholderText(u'聊天内容')
        text.setGeometry(0,0,400,380)
        text.setFont(QFont('微软雅黑',10))
        text.setStyleSheet('QWidget{background-color:rgb(255,255,255,80%)}')  #设置控件透明度
        #用户列表
        text_user = QTextEdit(self)#QTextEdit() QTextBrowse()
        # text_user.setEchoMode(QLineEdit.Password)
        text_user.setPlaceholderText(u'用户列表')
        text_user.setStyleSheet('QWidget{background-color:rgb(255,255,255,75%)}')
        text_user.setGeometry(400,0,400,380)
        self.text1= text_user
        #写入聊天信息
        text2 = QTextEdit(self)#QTextEdit() QTextBrowse()
        text2.setPlaceholderText(u'聊天内容')
        text2.setStyleSheet('QWidget{background-color:rgb(255,255,255,80%)}')
        text2.setGeometry(0,380,600,120)
        self.text2=text2
        #按钮
        button = QPushButton('发送',self)
        button.setFont(QFont('微软雅黑',8,QFont.Bold))
        button.setGeometry(530,470,100,30)
        self.button=button
    def push_send(self):
        while 1:
            self.button.clicked.connect(self.send_msg)
            time.sleep(0.1)
    def send_msg(self):
        self.text_content = self.text2.toPlainText()
        if len(self.text_content) != 0:
            print(self.text_content)
            self.c.send(self.text_content.encode())
            self.text2.clear()
            self.text_content = ''
    def show_msg(self):
        user_len = 0
        while 1:
            data = self.c.recv(1024).decode()
            if len(data) != 0:
                self.text.append(data.split('&')[1])
            if len(eval(data.split('&')[0])) != user_len:
                #self.text_user.setPlainText("")
                d = eval(data.split('&')[0])
                for i in d:
                    if d[i] not in self.text_user.toPlainText():
                        self.text_user.append(d.get(i))
                user_len = len(eval(data.split('&')[0]))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # trans = QWidget()
    # trans.setWindowOpacity(0.5)
    # trans.show()
    dialog = Login()
    # dialog.show()
    sys.exit(app.exec())