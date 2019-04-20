# encoding=utf-8
import HTMLTestRunnerCN
import unittest
class myclass:
    def sum (slef,a,b):
        return  a+b #将两个参数进行相加操作
    def sub(self,a,b):
        return  a-b #将两个参数进行相减的操作
class mytest(unittest.TestCase):
    def setUp(self):
        self.myclass=myclass()
        print('test start')
        self.a=3
        self.b=1
    def testsum(self):
        #断言亮数之和为4
        self.assertEqual(myclass.sub(self.a,self.b),4,'test sum fail')
    def testsub(self):
        #断言两数之差为2
        self.assertEqual(myclass.sum(self.a,self.b),2,'test sub fail')
    def tearDown(self):
        print('test end')
if __name__=='__main__':
    # unittest.main() #启动单元测试
    suit1=unittest.TestLoader().loadTestsFromTestCase(mytest)
    suit=unittest.TestSuite(suit1)
    filename='C:\\Users\\Administrator\\Desktop\\test9.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='测试报告',description='Report_description')
    runner.run(suit)
    fp.close()