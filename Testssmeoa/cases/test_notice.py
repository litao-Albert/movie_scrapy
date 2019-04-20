
from Testssmeoa.common.login import login
from Testssmeoa.common.setup import Setup
from Testssmeoa.common.oa_notice import notice
class test_notice:
    def count(self,newlist):
        ws=Setup().ws #得到driver对象
        l=login()#实例化登录
        l.get_wd(ws) #把driver传给登录的类，执行登录
        l.login_action('admin','admin') #登录
        n=notice()#实例化公告管理的类
        n.get_wd(ws) #将已经登录的driver对象交给公共管理模块
        n.notice(newlist) #执行公告管理新增
# if __name__=='__main__':
#     d=cass()
#     d.count(newlist='woniu')
