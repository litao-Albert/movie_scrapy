from TestTinyShop前台.cases.test_login import test_login
from TestTinyShop前台.get_date.readExcel import readExcel
import unittest
import sys
import HTMLTestRunnerCN
class test1:
    def __init__(self):
         self.r=readExcel().get_source()
         print('test start')
    def testcase(self):
         r=self.r
         for i in range(1,r.nrows):
            list=r.row_values(i) #得到所有的数据并返回一个列表
            newlist=list[2:3]  #切片得到一个新的列表
            newlist1=list[3:4]
            newlist2=list[2:5]
            print(newlist2)
            __import__('TestTinyShop前台.cases.'+list[0]) #动态引入
            m=sys.modules['TestTinyShop前台.cases.'+list[0]] #导入模块
            ca=getattr(m,list[0])#根据list[0]这个字符串获取到类
            ca=ca()#实例化该对象
            mtd=getattr(ca,list[1]) #根据list[1]这个字符串获取到方法
            mtd(newlist,newlist1)
test1().testcase()
# if __name__=='__main__':
#      suit=unittest.TestLoader().loadTestsFromTestCase(test1)
#      suit1=unittest.TestSuite(suit)
#      filename='C:\\Users\\Administrator\\Desktop\\test6.html'
#      fp=open(filename,'wb') #打开文件 并写入
#      runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
#      runner.run(suit1)
#      fp.close() #关闭文件




