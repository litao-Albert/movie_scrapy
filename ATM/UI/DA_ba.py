import pymysql
sql="""
   use woniuxu;
   create table user(
   user varchar(20),
   passwd varchar(20),
   money varchar(20)
   )
   ENGINE=InnoDB DEFAULT CHARSET=UTF8;
"""
ins="""
   use woniuxu;
   insert into user values('admin','123','5000');
   insert into user values('woniu','456','2000');
   insert into user values('litao','201403','1000000');
"""
ddd="""
   use woniuxu;
   insert into user values('764114271','2014','30000');
"""
sel="""
    use school;
    select * from user;
"""
ddd="""
    use woniuxu;
    drop table user;
"""
sdf="""
   use woniuxu;
   insert into user values('asd','789','3000');
"""
# db=pymysql.connect('localhost','root','','woniuxu',charset='utf8')
# cur=db.cursor()
# cur.execute(sel)
# db.commit()
# result=cur.fetchall()
# print(result)
# db.close()

def con_db(host='localhost',user='root',pwd='123456',database=None):
    db=pymysql.connect(host,user,pwd,database,charset='utf8')
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
    result=cur.fetchall()
    # print(result)
    return result
    print(result)
    db.close()
select_one_sql('select * from score',databasename='school')
# execute_sql(ins,databasename='woniuxu')
