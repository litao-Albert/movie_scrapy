# encoding=utf-8
import  unittest
from TestTinyShop后台.cases.test_sale import test_sale
from nose_parameterized import parameterized
from TestTinyShop后台.database1.de_ta import detabase
from selenium import webdriver
from threading import Thread
import time
import  random
import HTMLTestRunnerCN
class TinyShop(unittest.TestCase):
    def setUp(self):
        self.ws=webdriver.Firefox()
        self.ws.maximize_window()
        self.ws.get('http://172.16.0.145/index.php?con=simple&act=login')
        self.ws.implicitly_wait(30)
        self.h=detabase().exe_sql_one('select name from tiny_user',databasename='qew')
        print('test start')
    def testsearch(self):
        self.ws.find_element_by_id('account').clear()
        self.ws.find_element_by_id('account').send_keys('test1@qq.com')
        self.ws.find_element_by_name('password').clear()
        self.ws.find_element_by_name('password').send_keys('123456')
        self.ws.find_element_by_xpath('/html/body/div[2]/div/div/form/ul/li[4]/button').click()
        self.ws.find_element_by_id('search-keyword').clear()
        self.ws.find_element_by_id('search-keyword').send_keys('iphone')
        self.ws.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/button').click()
        # 断言搜索功能是否可以用
        try:
            self.ele1=self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/dl/dd/ul/li[1]/dl/dd[2]/span').text
            if '￥4898.00'==self.ele1:
                print('搜索功能可用')
        except:
            print('搜索功能不可用')
        assert '商品筛选'in self.ws.page_source,'搜索框可用'
    def tearDown(self):
        self.ws.quit()
        print('test end')
class TinyShop1(unittest.TestCase):
    def setUp(self):
        self.ws=webdriver.Firefox()
        self.ws.maximize_window()
        self.ws.get('http://172.16.0.145/index.php?con=simple&act=login')
        self.ws.implicitly_wait(30)
        print('test start')
        list=['服装','手机商城']
        self.ran=random.choice(list)
        list1=[1,2,3,4,5,6,7,8,9,10]
        self.y=random.choice(list1)
        self.l=detabase().exe_sql_one('select name from tiny_user',databasename='qew')
    def testbuygoods(self):
        self.ws.find_element_by_id('account').clear()
        self.ws.find_element_by_id('account').send_keys(self.l)
        self.ws.find_element_by_name('password').clear()
        self.ws.find_element_by_name('password').send_keys('123456')
        self.ws.find_element_by_xpath('/html/body/div[2]/div/div/form/ul/li[4]/button').click()
        handle1=self.ws.current_window_handle
        self.ws.find_element_by_link_text(self.ran).click()
        self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/dl/dd/ul/li[%d]/dl/dt/a/img'%self.y).click()
        #颜色
        self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div/dl[1]/dd/ul/li/span').click()
        #尺码
        self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div/dl[2]/dd/ul/li[1]/span').click()
        # 立即购买
        self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div/dl[5]/dd/a[1]/span').click()
        self.ws.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/p/a[2]').click()#立即结算
        #提交订单
        self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[6]/p/input').click()
        # 立即支付
        self.ws.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[3]/p/input').click()
        try:
             ele=self.ws.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/p/a[1]').text
             if  '继续购物'==ele:
                 print('购买成功')
        except :
            print('购买失败')
    def tearDown(self):
        self.ws.quit()
        print('test end')
if __name__=='__main__':
    # unittest.main()
    suit1=unittest.TestLoader().loadTestsFromTestCase(TinyShop)
    suit2=unittest.TestLoader().loadTestsFromTestCase(TinyShop1)
    suit=unittest.TestSuite([suit1,suit2])
    # unittest.TextTestRunner(2).run(suit)
    filename='C:\\Users\\Administrator\\Desktop\\test11.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')
    runner.run(suit)
    fp.close()