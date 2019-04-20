from selenium import webdriver
class login:
        def get_wd(self,webdriver):
         self.ws=webdriver
        def input_username(self,name):
            self.ws.find_element_by_name('name').clear()
            self.ws.find_element_by_name('name').send_keys(name)
        def input_password(self,password):
            self.ws.find_element_by_name('password').clear()
            self.ws.find_element_by_name('password').send_keys(password)
            self.ws.find_element_by_name('verifyCode').send_keys('aaaa')
        def button(self):
         self.ws.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
        #封装整个登录
        def testlogin(self,name,password):
            self.input_username(name)
            self.input_password(password)
            self.button()
            return  self.ws
