# encoding=utf-8
import  unittest
import random
from  HTMLTestRunner import HTMLTestRunner


class SuitTestSequenceFnctions(unittest.TestCase):
    def setUp(self):
        #初始化一个递增序列
        self.seq=range(10)
        print('test start')
    def runText(self):
        #从序列seq中随机选取一个元素
        element=range.choice(self.seq)
        #验证随机元素确实属于列表中
        self.assertTrue(element in self.seq,'ok')
class SuitTestDictValueFormatFubctions(unittest.TestCase):
    def setUp(self):
        self.seq=range(10)
    def test_shuyffle(self):
        #随机打乱原seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq,range(10))
        #验证执行函数时抛出了TypError异常
        self .assertRaises(TypeError,random.shuffle,(1,2,3))
    def tearDown(self):
        print('test end')
if __name__ == '__main__':
    # unittest.main()
    suite1=unittest.TestLoader().loadTestsFromTestCase(SuitTestDictValueFormatFubctions)
    suite2=unittest.TestLoader().loadTestsFromTestCase(SuitTestSequenceFnctions)
    suite=unittest.TestSuite([suite1,suite2])
    filme='C:\\Users\\黎涛\Desktop\\test0.html'
    fp=open(filme,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')
    runner.run(suite)


