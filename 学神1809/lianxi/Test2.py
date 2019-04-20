#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/12 10:48
# software:PyCharm Community Edition
# student = {
#     "name": "黎涛",
#     "age": 18,
#     "major": "Python"
# }
# cd = student.get("major")
# print(cd)
# school = {
#     "Python":[],
#     "Linux":[]
#         }
# cr = school["Python"]
# print(cr)

class People(object):
    country = 'china'
    @classmethod
    def getcountry(cls):
        return cls.country
    @ classmethod
    def setcountry(cls,country):
        cls.country = country
        return cls.country
p = People()
print(p.getcountry())
print(People.getcountry())
print(p.setcountry("litao"))

class Game(object):
    def __init__(self,playe_name):
        self.plave_name= playe_name
        Game.show_help()
        Game.show_top_score()
    @staticmethod
    def show_help():
        print("11111")
    @classmethod
    def show_top_score(cls):
        print("1111")
    def start_game(self):
        print('%s开始游戏'%(self.plave_name))

G = Game("litao")
G.start_game()
