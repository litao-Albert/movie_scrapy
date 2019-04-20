import time
from selenium import webdriver
from TestTinyShop前台.common.Setup1 import Setup

class login:
    def get_wd(self,webdriver):
        self.ws=webdriver
    def input_username(self,username):
        self.ws.find_element_by_id('account').clear() #清空用户名
        self.ws.find_element_by_id('account').send_keys(username) #写入用户名
    def input_password(self,password):
        self.ws.find_element_by_name('password').clear()
        self.ws.find_element_by_name('password').send_keys(password)
    def click_login_button(self):
        self.ws.find_element_by_xpath('/html/body/div[2]/div/div/form/ul/li[4]/button').click()
        self.ws.quit()
    #封装整个登录动作
    def login_action(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()
        return  self.ws
