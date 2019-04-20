import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class smeoa:
    def __init__(self):
        self.ws=webdriver.Firefox() #获取网页
        self.ws.maximize_window() #得到全屏
        self.ws.get('http://localhost/smeoa/index.php?m=login&a=index') #输入网址
        self.login()
        self.manage()
    def login(self):
        ws=self.ws
        ws.find_element_by_id('emp_no').clear() #清空用户名
        ws.find_element_by_id('emp_no').send_keys('admin') #输入用户名
        ws.find_element_by_id('password').clear() #清空密码
        ws.find_element_by_id('password').send_keys('admin') #输入密码
        # ws.switch_to.frame(ws.find_element_by_class_name('col-sm-offset-3 col-sm-9'))
        ws.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/form/div[4]/div/input').click()
    def manage(self):
        time.sleep(2)
        ws=self.ws
        ws.find_element_by_link_text('管理').click()
        time.sleep(1)
        ws.find_element_by_link_text('公司信息管理').click()
        time.sleep(1)
        ws.find_element_by_link_text('组织图').click()
        time.sleep(1)
        ws.find_element_by_link_text('小微企业').click()
        Select(ws.find_element_by_id('dept_grade_id')).select_by_index(0)
        ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/form/div[5]/div/div/span/button').click()
        ws.switch_to.frame(ws.find_element_by_class_name('myFrame'))
        time.sleep(1)
        # ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/ul/li/ul/li/ul/li[1]/a/span').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/ul/li/ul/li/ul/li[1]/a/span').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/div[1]/a').click()
        #ws.find_element_by_link_text('关闭').click()
        ws.switch_to.default_content()
        ws.find_element_by_id('sort').send_keys('01')
        Select(ws.find_element_by_id('is_del')).select_by_index(0)
        # ws.switch_to.frame(ws.find_element_by_class_name('myFrame'))
        ele2=ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/form/div[8]/div/textarea')
        ele2.send_keys('你是sb')
        ws.find_element_by_link_text('新增').click()
        time.sleep(2)
        ws.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button').click()
        #职位
        ws.find_element_by_link_text('职位').click()
        time.sleep(1)
        ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[2]').click()
        ws.find_element_by_id('position_no').send_keys('07')
        ws.find_element_by_link_text('新增').click()
        #职级
        time.sleep(4)
        ws.find_element_by_link_text('职级').click()
        time.sleep(1)
        ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[2]').click()
        ws.find_element_by_id('rank_no').send_keys('GR50')
        ws.find_element_by_link_text('新增').click()
        time.sleep(4)
        #员工登记
        ws.find_element_by_link_text('员工登记').click()
        Select(ws.find_element_by_id('eq_is_del')).select_by_index(0)
        time.sleep(1)

        ws.find_element_by_id('emp_no').send_keys('1008')#员工编号
        ws.find_element_by_id('name').send_keys('总经理张三') #姓名
        Select(ws.find_element_by_id('sex')).select_by_index(0) #性别
        time.sleep(1)
        ele=ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/form/table/tbody/tr[5]/td[1]/div/div/a')
        ele.click()#部门
        time.sleep(1)
        ws.switch_to.frame(ws.find_element_by_class_name('myFrame')) #获取节点
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[3]/ul/ul/li[1]/ul/li[1]/ul/li[1]/a/span').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div/div[1]/a').click()
        ws.switch_to.default_content()
        time.sleep(2)
        Select(ws.find_element_by_id('rank_id')).select_by_index(1) #职级
        time.sleep(1)
        Select(ws.find_element_by_id('position_id')).select_by_index(2) #职位
        time.sleep(1)
        ws.find_element_by_id('office_tel').send_keys('023-76542221')#办公室电话
        ws.find_element_by_id('mobile_tel').send_keys('1876545723')#移动电话
        time.sleep(1)
        ws.find_element_by_id('email').send_keys('783343@qq.com') #电子邮箱
        ws.find_element_by_id('duty').send_keys('负责招生')
        Select(ws.find_element_by_id('is_del')).select_by_index(0)#状态
        time.sleep(1)
        ws.find_element_by_link_text('新增').click()
        time.sleep(1)
        ws.find_element_by_link_text('确定')
    def __del__(self):
        time.sleep(3)
        self.ws.quit()

smeoa()