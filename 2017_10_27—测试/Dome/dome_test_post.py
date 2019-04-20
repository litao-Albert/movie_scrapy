import requests
import json
import unittest
class info:
     def __init__(self):
        self.url='http://127.0.0.1:8000/api/sec_add_event/'

     def test(self,a,b,c,d):
        date={'eid':a,'name':b,'limit':c,'address':d}
        self.r=requests.post(self.url,params=date)
        self.result=self.r.json()
        return self.result
     def test1(self,a,b,c,d):
        date={'eid':a,'name':b,'limit':c,'address':d}
        r=requests.post(self.url,params=date)
        result=r.json()
        return result
class Test_count(unittest.TestCase):
    def setUp(self):
        print('test start....')
        self.info=info()
    def test1(self):
        self.test_one=info.test(1,'蜗牛学院',5,'蜀都中心')
        self.assertEqual(self.test_one['status'],10024)
    def test2(self):
        pass #传入的name为int 地址也为int是否会成功
    def tearDown(self):
        print('test end....')
if __name__=='__main__':
   unittest.main()