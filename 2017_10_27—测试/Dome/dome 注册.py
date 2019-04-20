import requests
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import  time

class phpwind:
    def register(self,username,password,message):
        driver = webdriver.Firefox()
        driver.get('http://localhost/upload')
        driver.implicitly_wait(30)
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/ul/li/input').click()
        driver.find_element_by_id("regname").clear()
        driver.find_element_by_id("regname").send_keys(username)
        time.sleep(2)
        driver.find_element_by_id("regpwd").clear()
        driver.find_element_by_id("regpwd").send_keys(password)
        driver.find_element_by_id("regpwdrepeat").clear()
        driver.find_element_by_id("regpwdrepeat").send_keys(password)
        driver.find_element_by_id("regemail").clear()
        driver.find_element_by_id("regemail").send_keys(message)
        driver.find_element_by_css_selector("dd > input.btn").click()
        print('注册成功')
    def tearDown(self):
        self.driver.quit()
phpwind().register()

# s=requests.session()
# url='http://localhost/upload/register.php?nowtime=1509766083909&verify=4d4a908e'
# dates={'forward':'','step':'2','regname':'123456','regpwd':'123456','regpwdrepeat':'123456','regemail':'764114278%40QQ.com','rgpermit':'1'}
# s.post(url,data=dates)
