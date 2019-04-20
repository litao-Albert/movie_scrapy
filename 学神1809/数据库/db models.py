#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/19 10:24
# software:PyCharm Community Edition

import pymysql
use = '''
use school
'''
sql = '''
create table student1(id int primary key auto_increment,name varchar(30)
,age int)
'''

# while True:
#     name = input('请输入你想要插入得名字：')
#     age = input('请输入插入这个人对应得年龄：')
inr = '''
insert into student1(name,age) value(%s,%s)
'''
sle = '''
select * from student1
'''
class Database(object):

    def db_connect(self,host='localhost',use='root',pwd='123456',database=None):
        db = pymysql.connect(host,use,pwd,database)
        return db
    def py_execute(self,sql,databasename=None):
        db = self.db_connect(database=databasename)
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()
    def selec_one(self,sql,databasename = None):
        db = self.db_connect(database=databasename)
        cur = db.cursor()
        cur.execute(sql)
        reslut = cur.fetchone()
        cur.close()
        db.close()
D = Database()
D.py_
