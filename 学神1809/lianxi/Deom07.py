# 定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高分数的课程。get_course()
# 4 返回该学生的平均成绩get_avg()
class student:
    # name="lt"
    # age=20
    # score={'语文':90,'数学':96,'英语':95}
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_max(self):
        li_values=list(self.score.values()) #获取字典中所有的值，并返回一个列表
        m=max(li_values) #从列表中获取最大的值
        for i in self.score: # 遍历一个字典 取每一个key
            if self.score.get(i)==m: #通过key找值，并验证是否是最大值
                print(i)
    def get_avg(self):
        li=list(self.score.values()) #获取字典中的所有值，并返回一个列表
        print(sum(li)/len(li))
name=input('姓名：')
age=int(input('年龄：'))
score=input('成绩：')
s=student(name,age,eval(score))
s.get_avg()
s.get_age()
s.get_name()
s.get_max()
