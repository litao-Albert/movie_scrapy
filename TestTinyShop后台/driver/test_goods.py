from TestTinyShop后台.cases.test_goods import start_test
from TestTinyShop后台.get_date.readexcel import readExcel
import sys
class cass:
    def __init__(self):
        self.r=readExcel().get_source()
    def start_case(self):
        r=self.r
        for i in range(1,r.nrows):
            list=r.row_values(i) #得到所有的数据并返回一个列表
            __import__('TestTinyShop.cases.'+list[0]) #动态引入
            m=sys.modules['TestTinyShopcases.'+list[0]]#导入模块
            ca=getattr(m,list[0])#根据list[0]这个字符串获取到类
            ca=ca()#实例化该对象
            mtd=getattr(ca,list[1])#根据list[1]这个字符串获取到方法

