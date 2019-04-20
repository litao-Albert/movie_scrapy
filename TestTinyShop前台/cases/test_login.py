from TestTinyShop前台.common.Setup1 import Setup
from TestTinyShop前台.common.login前台 import login
from TestTinyShop前台.get_date.readExcel import readExcel
class test_login:
    def count(self,newlist,newlist1):
        ws=Setup().ws#实例化Setup()对象
        l=login()#调用登录方法
        l.get_wd(ws) #把driver传给登录的类，执行登录
        l.login_action(newlist,newlist1)



