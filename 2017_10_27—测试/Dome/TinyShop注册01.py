from selenium import  webdriver

class TinyShop:
    def __init__(self):
        self.ws=webdriver.Firefox()
        self.ws.maximize_window()
        self.ws.get('http://172.16.0.145/index.php?con=simple&act=reg')
        self.ws.implicitly_wait(30)
    def degister(self,username):
        self.ws.find_element_by_id('email').click()
        self.ws.find_element_by_id('email').send_keys(username)
        self.ws.find_element_by_name('password').send_keys('123456')
        self.ws.find_element_by_name('repassword').send_keys('123456')
        self.ws.find_element_by_id('verifyCode').send_keys('aaaa')
        self.ws.find_element_by_id('readme').click()
        self.ws.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/ul/li[6]/button').click()
        self.ws.quit()
for i in range(100,600):
    a=str(i)
    b='test'+a
    username=b+'@qq.com'
    TinyShop().degister(username)
