#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/12 10:28
# software:PyCharm Community Edition

class Corce:
    def __init__(self):
        print("_________________________________")
        self.school = {
            "Python":[],
            "Linux":[]
        }
    def register(self,major,student):
        if major in self.school:
            self.school[major].append(student)
            print("报名成功")
        else:
            print("你需要报得课程不在这里")
if __name__ == "__main__":
    student = {
        "name":"黎涛",
        "age":18,
        "major":"Python"
    }
    cd = Corce()
    cd.register(student.get("major"),student)
    print(cd.school)
    print("——————————————————")