import pymysql
sql = ''

class Database(object):
    def con_db(self,host='localhost',user='root',pwd='123456',database=None):
        db = pymysql.connect(host,user,pwd,database)
        return db
    def cur_db(self,sql,databasename=None):
        db =self.con_db(database=databasename)
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()
    def select_db(self,sql,databasename=None):
        db = self.con_db(database=databasename)
        cur = db.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        print(result)
        db.commit()
        cur.close()
        db.close()

D = Database()
D.select_db('select * from student',databasename='school')
