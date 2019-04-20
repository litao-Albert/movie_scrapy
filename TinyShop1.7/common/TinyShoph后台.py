import  unittest
from selenium import webdriver
class TinyShop(unittest.TestCase):
    def setUp(self):
        self.ws=webdriver.Firefox()
        self.ws.maximize_window()
        self.ws.get('http://172.16.0.22/TinyShop_v1.7/index.php?con=admin&act=login')
        self.ws.implicitly_wait(30)
        print('test start')
    def testlogin(self):
        self.ws.find_element_by_name('name').clear()
        self.ws.find_element_by_name('name').send_keys('admin')
        self.ws.find_element_by_name('password').clear()
        self.ws.find_element_by_name('password').send_keys('123456')
        self.ws.find_element_by_name('verifyCode').send_keys('aaaa')
        self.ws.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
        assert '商品中心'in self.ws.page_source
    def tearDown(self):
        self.ws.quit()
        print('test end')
if __name__=='__main__':
    unittest.main()
