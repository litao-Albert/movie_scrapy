from Testssmeoa.common.setup import Setup
import time
class login:
     def get_wd(self,webdriver):
        self.ws = webdriver
     #用户名
     def input_username(self,username):
       self.ws.find_element_by_id('emp_no').clear() #清空用户名
       self.ws.find_element_by_id('emp_no').send_keys(username) #输入用户名
     #密码
     def input_password(self,password):
       self.ws.find_element_by_id('password').clear() #清空密码
       self.ws.find_element_by_id('password').send_keys(password) #输入密码
        # ws.switch_to.frame(ws.find_element_by_class_name('col-sm-offset-3 col-sm-9'))
     #登录
     def click_login_button(self):
      self.ws.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/form/div[4]/div/input').click()
     # 封装登录动作的方法
     def login_action(self,username,password):
         self.input_username(username)
         self.input_password(password)
         self.click_login_button()
         return self.ws
#      # 封装整个登录操作的方法
#      def login_fast(self,username,password):
#          st=Setup()
#          self.ws=st.ws
#          self.login_action(username,password)
#          return self.ws



