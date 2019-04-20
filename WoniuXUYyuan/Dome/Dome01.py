import pymysql
sql="""
   use woniudb;
   create table student(
   id int primary key,
   name varchar(20),
   age int,
   sex varchar(20),
   class varchar(20)
   )
   ENGINE=InnoDB DEFAULT CHARSET=UTF8;

"""

ins="""
   use woniudb;
   insert into student values(5,'二师兄',25,'男','21期');


"""
add="""
   use woniudb;
   drop table student;
"""
sel="""

   select name from student
"""
upd="""
   use woniudb;
   update student set sex='女' where class='6班';
"""

# db=pymysql.connect('localhost','root', '','woniudb',charset='utf8',)
# cur=db.cursor()
# cur.execute(sel)
# db.commit()
# result=cur.fetchmany(4)
# print(result)
# db.close()


def con_db(host='localhost',user='root',pwd='',database=None):
    db=pymysql.connect(host,user,pwd,database,charset='utf8')
    return db
def execute_sql(sql,datebasename=None):
    db=con_db(database=datebasename)
    cur=db.cursor()
    cur.execute(sql)
    db.close()
def select_one_sql(sql,databasename=None):
    db=con_db(database=databasename)
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
    result=cur.fetchall()
    print(result)
    db.close()
select_one_sql('select name from student',databasename='woniudb' );
execute_sql(ins,datebasename='woniudb');