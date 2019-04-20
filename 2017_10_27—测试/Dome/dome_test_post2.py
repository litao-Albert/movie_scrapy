import requests,unittest,time
import hashlib
class Test_count(unittest.TestCase):
    def setUp(self):
        s=time.time()
        self.s1=int(self.s)
        print('test start...')
        self.url = 'http://127.0.0.1:8000/api/add_event/'
        md5=hashlib.md5()
        sign_str=str(int(self.s))+'&Guest-Bugmaster'
        sign_byte=sign_str.encode()
        self.md5.update(sign_byte)
        self.sign_md5=self.md5.hesdigest
        print(self.sign_md5)
    def test_post_exist(self):
        datas = {'eid':23,'name':'27期测试','limit':1000,'address':'天津','start_time':'2017-11-11 12:00:00','time':self.s1,'sign':self.sign_md5}
        r = requests.post(self.url,data = datas)
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'event id already exists')

    def test_post_add(self):
        datas = {'eid':25,'name':' 红米手机','limit':500,'address':'酉阳','start_time':'2017-11-09 14:00:00'}
        r = requests.post(self.url,data = datas)
        result = r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'add event success')

    def test_post_add2(self):
        datas = {'eid':57,'name':' 蜗牛学院','limit':500,'address':'重庆','start_time':'20171111 14:00:00'}
        r = requests.post(self.url,data = datas)
        result = r.json()
        self.assertEqual(result['status'],10024)

    def test_post_params_error(self):
        datas = {'eid':57,'name':'  蜗牛学院','limit':500,'address':'重庆'}
        r = requests.post(self.url,data = datas)
        result = r.json()
        self.assertEqual(result['status'],10021)

    def test_post_sign(self):
        datas = {'eid':66,'name':' iphone','limit':800,'address':'江津','start_time':'2017-11-09 14:00:00','time':time.time(),'sign':''}
        r = requests.post(self.url,data = datas)
        result = r.json()
        self.assertEqual(result['status'],10012)
    def tearDown(self):
        print('test end...')
if __name__ == '__main__':
    unittest.main()