import unittest
from time import sleep

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class LoveHoseTest(unittest.TestCase):
    def setUp(self):
        url = 'https://passport.5i5j.com/passport/login?service=https%3A%2F%2Fbj.5i5j.com%2Freglogin%2Findex%3FpreUrl%3Dhttps%253A%252F%252Fbj.5i5j.com%252F%253Fpmf_group%253Dbaidu%2526pmf_medium%253Dppzq%2526pmf_plan%253D%2525E5%2525B7%2525A6%2525E4%2525BE%2525A7%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_unit%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_keyword%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_account%253D160&status=1&city=bj'
        self.wd = webdriver.Firefox()
        self.wd.get(url)
    def login(self,username,password):
        sleep(1)
        user = self.wd.find_element_by_id('username')
        pawd = self.wd.find_element_by_id('password')
        submit = self.wd.find_element_by_id('login')
        user.send_keys(username)
        pawd.send_keys(password)
        submit.click()
    def test_longin(self):
        self.login('15213756843','litao201403')
        sleep(3)
        loginTest = self.wd.find_element_by_id('erromsg')
        self.assertEqual(loginTest,'用户名或密码错误')
    def tearDown(self):
        self.wd.close()
if __name__ == "__main__":
    # unittest.main()
    # 实例化测试用例容器
    sut=unittest.TestSuite()
    #添加测试
    sut.addTest(LoveHoseTest("test_longin"))
    # 生成报告
    with open('jon.html','w+') as fb:
        runner = HTMLTestRunner(stream = fb,title = 'testExample',description = 'this is our Test')
    runner.run(sut)