from TestTinyShop后台.common.Setup import Setup2
from  TestTinyShop后台.common.Login import login
from  TestTinyShop后台.common.订单中心 import sale
class test_sale:
    def count(self):
        ws=Setup2().ws
        l=login()
        l.get_wd(ws)
        l.testlogin('admin',123456)
        s=sale()
        s.get_wd(ws)
        s.test_sale()
# test_sale().count()