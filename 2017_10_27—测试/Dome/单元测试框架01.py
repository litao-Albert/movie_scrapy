# _*_ coding:utf-8 _*_
import unittest
import HTMLTestRunner
import math
class Calc(object):
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
class SuitTestCale(unittest.TestCase):
    def setUp(self):
        self.c=Calc()
        print('strat test')
    def test_Sub(self):
        self.assertEqual(self.c.sub(100,34),66,'求差结果错误')
    def test_Add(self):
        self.assertEqual(self.c.add(1,32),33,'求和结果错误')
    def tearDown(self):
        print('test end')
class SuitTestPow(unittest.TestCase):
    def setUp(self):
        self.seq=range(10)
    def test_pow(self):
        self.assertEqual(pow(6,3),216,'求米结果错误')
    def test_hasatta(self):
        self.assertTrue(hasattr(math,'pow'),'检测的属性不存在')
    def tearDown(self):
        print('test end')
if __name__=='__main__':
    # unittest.main()
    suit1=unittest.TestLoader().loadTestsFromTestCase(SuitTestCale)
    suit2=unittest.TestLoader().loadTestsFromTestCase(SuitTestPow)
    suit=unittest.TestSuite(suit1)
    filename='C:\\Users\\Administrator\\Desktop\\test6.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')
    runner.run(suit)
    # unittest.TextTestRunner(verbosity=2).run(suit)
