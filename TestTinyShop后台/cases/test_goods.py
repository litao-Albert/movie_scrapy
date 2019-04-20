from  TestTinyShop后台.common.Login import login
from  TestTinyShop后台.common.Setup import Setup2
from  TestTinyShop后台.common.商品上架 import good
class start_test:
    def count(self,):
        ws=Setup2().ws #实例化Setup2()对象
        l=login()#调用登录方法
        l.get_wd(ws)#将driver传给登录执行登录
        l.testlogin('admin',123456)
        g=good()
        g.get_wd(ws) #把执行登录的页面的
        g.test_goods()
        g.selectone()
        g.selecttwo()
        g.selectthree()
start_test().count()
