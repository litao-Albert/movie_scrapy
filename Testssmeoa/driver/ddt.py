from Testssmeoa.get_date.readExcel import readExcel
from Testssmeoa.cases.test_notice import notice
import sys
class ddt:
    def __init__(self):
        self.r=readExcel().get_source()
    def start_testcase(self):
        r=self.r
        for i in range(1,r.nrows):
            list=r.row_values(i) #得到所有的数据并返回一个列表
            newlist=list[2:10]  #切片得到一个新的列表
            print(newlist)
            __import__('Testssmeoa.cases.'+list[0])#动态引入
            m=sys.modules['Testssmeoa.cases.'+list[0]] #导入模块
            ca=getattr(m,list[0])#根据list[0]这个字符串获取到类
            ca=ca()#实例化该对象
            mtd=getattr(ca,list[1]) #根据list[1]这个字符串获取到方法
            mtd(newlist)

ddt().start_testcase()

