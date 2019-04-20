import  pymysql
import random
sql='''
for i in range(6,100):
    insert into tiny_address(id,user_id,accept_name,mobile,phone,province,city,county,zip,addr,is_default) VALUES
       (5,5,13589100333,'黎明',13589100475,370000,370100,370102,250000,12345,1);
'''
sns='''
   select name from tiny_user;
'''
ins='''
    insert into SC values(2,'C4',90.8);
'''
nal='''
select * from tiny_address;
'''
class detabase:
    def con_db(self,host='172.16.0.145',user='root',pwd='123456',database=None):
        db=pymysql.connect(host,user,pwd,database,charset='utf8')
        return db
    def db_cur(self,sql,databasename=None):
        db=self.con_db(database=databasename)
        cur=db.cursor()
        cur.execute(sql)
        db.commit()
        db.close()
    def exe_sql_one(self,sql,databasename=None):
        db=self.con_db(database=databasename)
        cur=db.cursor()
        cur.execute(sql)
        result=cur.fetchall()
        l=list(result)
        ls=random.choice(l)
        return ls[0]
        db.commit()
        db.close()
# detabase().db_cur(sql,databasename='qew')
detabase().exe_sql_one('select name from tiny_user',databasename='qew')



