import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class smeoa:
    def __init__(self):
        self.wd=webdriver.Firefox() #获取网页
        self.wd.maximize_window() #得到全屏
        self.wd.get('http://localhost/smeoa/index.php?m=login&a=index') #输入网址
        self.wd.implicitly_wait(30)
        self.login()
        self.notice()
    def login(self):
        wd=self.wd
        wd.find_element_by_id('emp_no').clear() #清空用户名
        wd.find_element_by_id('emp_no').send_keys('admin') #输入用户名
        wd.find_element_by_id('password').clear() #清空密码
        wd.find_element_by_id('password').send_keys('admin') #输入密码
        # ws.switch_to.frame(ws.find_element_by_class_name('col-sm-offset-3 col-sm-9'))
        wd.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/form/div[4]/div/input').click() #点击登录
    def notice(self):
        # time.sleep(2) #等待2秒进入下一步操作
        wd=self.wd
        wd.find_element_by_link_text('公告').click()
        wd.find_element_by_link_text('公告管理').click() #点击公告管理
        wd.find_element_by_id('name').clear() #清空名称里面的内容
        wd.find_element_by_id('name').send_keys('') #输入内容蜗牛学院
        ele=wd.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/form/div[2]/div/div/span/button')
        ele.click() #点击选择
        #ws.switch_to.frame(ws.find_element_by_class_name('popup_tree_menu panel-body'))
        wd.switch_to.frame(wd.find_element_by_class_name('myFrame'))#切换节点
        # time.sleep(1)
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/ul/li/a/span').click()
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/div[1]/a').click() #点击确定
        # time.sleep(1)
        wd.switch_to.default_content() #关闭节点
        # time.sleep(1)
        ls=wd.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/form/div[3]/div/div/a/i')
        ls.click() #进入管理
        wd.switch_to.frame(wd.find_element_by_class_name('myFrame')) #获取管理的节点
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/ul/li[4]/a/span').click()
        wd.switch_to.default_content() #关闭节点
        time.sleep(1)
        wd.switch_to.frame(wd.find_element_by_class_name('myFrame')) #获取节点

        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div/nobr[1]/label/span').click()
        time.sleep(2)
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div[2]/label/a/i').click()
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div[4]/label/a').click()
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div[6]/label/a').click()
        wd.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
        wd.switch_to.default_content()
        wd.find_element_by_id('sort').send_keys('01') #操作排序并写入01
        Select(wd.find_element_by_id('is_del')).select_by_index(1) #状态一栏
        #获取备注的路径
        # ws.switch_to.frame(ws.find_element_by_class_name('col-sm-9'))
        lg=wd.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/form/div[8]/div/textarea')
        lg.send_keys('欢迎来到蜗牛学院第27期测试学习') #在备注中写入内容
        time.sleep(1)
        #点击新增
        wd.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/a[1]').click()
        try:
            ele=wd.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/h5').text
            print(ele)
            if '请输入名称'==ele:
              print('新增失败')
        except:
            print('新增成功')
    def __del__(self):
     self.wd.quit()

smeoa()