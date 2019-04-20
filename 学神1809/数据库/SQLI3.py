#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/19 14:48
# software:PyCharm Community Edition
import sqlite3
import peewee
db = sqlite3.connect('school')
db1 =  peewee.SqliteDatabase('sql.db')
class Teacher(peewee.Model):
    name = peewee.CharField(max_length=20,default='litao')
    age = peewee.CharField()
    class Meta:
        database = db1
if __name__ == '__main__':

    # Teacher.create_table()
    # # 增加
    # T = Teacher()
    # T.name = 'litao'
    # T.age = 18
    # T.save()
    #
    # T = Teacher().insert(name='小龙女',age=18,)
    # T.execute()
    # # 删除
    # T = Teacher().delete().where(Teacher.id ==1)
    # T.execute()
    # #修改
    T = Teacher().update(name='for').where(Teacher.id ==1)
    T.execute()
    T = Teacher().get(id=2)
    T = Teacher().get_by_id(2)
    T.name = '杨过'
    T.save()

    # 查找
    T_list = Teacher.select()
    for i in T_list:
        print(i.name, i.age)

    T_list = Teacher.select().order_by(Teacher.age)
    for i in T_list:
        print(i.name, i.age)
    # 查一条
    T_list = Teacher.select().where(Teacher.age == 18)
    for i in T_list:
        print(i.name, i.age)
    T = Teacher.get(id=2)
    print(T.name, T.age)


