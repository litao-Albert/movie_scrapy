import json
import unittest
import requests
class info:
     def __init__(self):
        self.url='http://127.0.0.1:8000/api/add_event/'
     def test(self,a,b,c,d,e):
        s=requests.session()
        date={'eid':a,'name':b,'limit':c,'address':d,'start_time':e}
        r=s.post(self.url,params=date)
        result=r.json()
        return result
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
        self.assertEqual(self.info.test(1,'蜗牛学院',5,'蜀都中心','2016-09-11 12:00:00'))
    # def test2(self):
    #     self.assertEqual(self.info.test(1,123,5,5)) #传入的name为int 地址也为int是否会成功
    def tearDown(self):
        print('test end....')
if __name__=='__main__':
   unittest.main()