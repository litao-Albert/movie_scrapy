from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
class Login(QWidget):
    def __init__(self):
        QtGui,QWidget.__init__(self)  #初始化组件
        self.setGeometry(500, 300, 400, 300)  #指定窗体位置和大小
        self.setWindowTitle("chat")  #窗体设置标题
        palette=QtGui.QPalette()
        icon=QtGui.QPixmap('C:\\Users\\Administrator\\Desktop\\sights.jpg')
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon)) #添加背景图片
        self.setPalette(palette)
        self.addUI()
        self.show()
    def addUI(self): #添加各种组件
        labe=QLabel('xxxx管理系统',self)
        labe.setGeometry(120,30,200,40)
        labe.setFont(QFont('微软雅黑',18,QFont.Bold))
        lab1=QLabel('用户名：',self)
        lab1.setFont(QFont('微软雅黑',12,QFont.Bold))
        lab1.setGeometry(60,100,60,30)
        text=QLineEdit(self)

        text.setGeometry(130,100,200,30)
        lab2=QLabel('密 码：',self)
        lab2.setFont(QFont('微软雅黑',12,QFont.Bold))
        lab2.setGeometry(60,160,60,30)

        text2=QLineEdit(self)
        text2.setEchoMode(QLineEdit.Password)
        text2.setPlaceholderText(u'密码')
        text2.setGeometry(130,160,200,30)
        self.input=text
        button=QPushButton('登录',self)
        button.setFont(QFont('微软雅黑',10,QFont.Bold))
        button.setGeometry(270,220,60,30)
        self.button=button
if __name__=='__mian__':
    app=QApplication(sys.argv)
    dialog=Login()
    #dialog.show()
    sys.exit(app.exec())








