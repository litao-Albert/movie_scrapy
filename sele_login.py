from selenium import  webdriver
class smeoa:
    def __init__(self):
        self.wd=webdriver.Firefox() #获取网页
        self.wd.maximize_window() #得到全屏
        self.wd.get('http://localhost/smeoa/index.php?m=login&a=index') #输入网址
        self.wd.implicitly_wait(30)
        self.login()
    def login(self):
        wd=self.wd
        wd.find_element_by_id('emp_no').clear() #清空用户名
        wd.find_element_by_id('emp_no').send_keys('admin') #输入用户名
        wd.find_element_by_id('password').clear() #清空密码
        wd.find_element_by_id('password').send_keys('admin') #输入密码
        # ws.switch_to.frame(ws.find_element_by_class_name('col-sm-offset-3 col-sm-9'))
        wd.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/form/div[4]/div/input').click()
        try:
            ele=self.wd.find_element_by_link_text('公告').text
            if '公告'==ele:
                print('登录成功')
        except:
            print('登录失败')
    def __del__(self):
        self.wd.quit()
smeoa()