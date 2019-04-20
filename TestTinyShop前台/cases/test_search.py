from TestTinyShop前台.common.Setup1 import Setup
from TestTinyShop前台.common.login前台 import login
from TestTinyShop前台.common.search import search
class test_search:
    def count(self):
        ws=Setup().ws#实例化Setup()对象
        l=login()#调用登录方法
        l.get_wd(ws) #把driver传给登录的类，执行登录
        l.login_action('test1@qq.com',123456)
        s=search() #实例化搜索的类
        s.get_wd(ws)#将已经登录的模块交给Search
        s.search('iphone')
test_search().count()

