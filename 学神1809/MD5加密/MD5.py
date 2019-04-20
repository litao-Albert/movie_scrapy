#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/30 10:14
# software:PyCharm Community Edition
import hashlib

md5 = hashlib.md5()
md5.update('123456'.encode())
password = md5.hexdigest()
print(password)
user = {'name':'admin',"password":'e10adc3949ba59abbe56e057f20f883e'}
class Test_login(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self):
        md5 = hashlib.md5()
        md5.update(self.password.encode('utf-8'))
        password = md5.hexdigest()
        if self.username == user['name'] and user['password'] == password:
            print('欢迎进入LOL世界')
        else:
            print("用户名或者密码错误")
if __name__ == '__main__':
    username = input("请输入用户名:")
    password = input("请输入密码:")
    T = Test_login(username,password)
    T.login()
