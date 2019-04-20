#coding:utf-8
import pymysql
# db = pymysql.connect('localhost','root','123456','datebase','utf-8')  #连接数据库
# cur = db.cursor() #创建一个光标
# cur.execute() # 执行sql语句
# result = cur.fetchall() #查询并返回一个值
# db.commit() # 提交事务
# db.close() # 关闭链接
sql = """
select * from score;
     
"""
def con_db(host='localhost',user='root',pwd='123456',database=None):
    db = pymysql.connect(host,user,pwd,database,charset='utf-8')
    return db
def execute_sql(sql,databasename=None):
    db=con_db(database=databasename)
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()
def select_one_sql(sql,databasename=None ):
    db=con_db(database=databasename)
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
    result=cur.fetchmany(1)
    # print(result)
    return result
    print(result)
    db.close()
# execute_sql(sql,databasename='school');
select_one_sql('select * from score',databasename='school');