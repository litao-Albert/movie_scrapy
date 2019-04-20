import requests
import json
import unittest
#定义一个类用来请求get
class count1:
     def __init__(self):
        self.url='http://127.0.0.1:8000/api/get_event_list/'
     def test(self,a):
        date={'eid':a}
        r=requests.get(self.url,params=date)
        result=r.json()
        return result
     def test1(self,b):
         pass
#单元测试
class Test_count(unittest.TestCase):
    def setUp(self):
        print('test start....')
        self.url='http://127.0.0.1:8000/api/get_event_list/'
    def test1(self):
        r=requests.get('http://127.0.0.1:8000/api/get_event_list/')
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
    def test2(self):
         r=requests.get('http://127.0.0.1:8000/api/get_event_list/')
         result=r.json()
         self.assertEqual(result['date']['name'],'红米手机发布会')
    def tearDown(self):
        print('test end....')
if __name__=='__main__':
   unittest.main()
   # ut=unittest.TestSuite()
   # ut.addTest(count1('test_mut'))
   # run=unittest.TextTestRunner()
   # run,run(ut)
