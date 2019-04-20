#coding:utf-8
"""
     本文件用于描述文章数据模型，具体字段如下
      标题
      作者
      时间
     描述
     内容
"""


import peewee
#创建数据库连接
db = peewee.SqliteDatabase("blog.db")
#创建数据表
class Article(peewee.Model):
    title = peewee.CharField(max_length = 32)
    author = peewee.CharField(max_length = 32)
    time = peewee.CharField(max_length = 32)
    description = peewee.TextField()
    content = peewee.TextField()
    #数据库和数据表进行关联
    class Meta:
        database = db

if __name__ == "__main__":
    Article.create_table() #同步数据库