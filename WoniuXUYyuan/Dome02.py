import unittest
import requests
import json
from WoniuXUYyuan.Dome.Dome03 import count1
class Test_count(unittest.TestCase):
    def setUp(self):
        print('test start....')
        self.count1=count1()
    def test_add(self):
        self.assertEqual(self.count1.test())
    # def test_sub(self):
    #     self.assertEqual(self.count1.sub(3,6),-3)
    # def test_mut(self):
    #     self.assertEqual(self.count1.mut(6,3),18)
    # def test_div(self):
    #     self.assertEqual(self.count1.div(9,3),4)
    def tearDown(self):
        print('test end....')
if __name__=='__main__':
   unittest.main()
   ut=unittest.TestSuite()
   ut.addTest(count1('test_mut'))
   run=unittest.TextTestRunner()
   run,run(ut)