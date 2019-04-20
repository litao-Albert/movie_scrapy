class person():
   def __init__(self):
       print('njjnnj')
   def eat(self):
       print('人正在吃饭')
class teacher():
    def eat(self):
        print('老师正在吃饭')
    def get_name(self,name):
        return name
class student(person):
    def eat(self):
        print('学生正在吃饭')
    def get_name(self,name):
        return name
# student().eat()
class class_room:
    xiaoming=student()
    lt=teacher()
    def teach(self):
     print('%s正在给%s上课'%(self.lt.get_name('lt'),self.xiaoming.get_name('xiaoming')))
class_room().teach()
s=student()
s.__init__()