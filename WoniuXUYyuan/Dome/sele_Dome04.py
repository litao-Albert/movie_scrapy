from selenium import webdriver #导入selenium包
from selenium.webdriver.support.ui import Select#导入下拉列表包
from selenium.webdriver.support.ui import WebDriverWait#创建显示等待对象
import time
class selenium:
    def __init__(self):
        self.wd=webdriver.Firefox() #获取Firefox网页
        self.wd.maximize_window() #让网页全屏  窗口设置
        self.wd.get('http://www.baidu.com')  #输入网址

    def count(self):
        self.wd.find_element_by_id('kw').send_keys('蜗牛学院') #获取输入的文本框输入蜗牛学院
        self.wd.find_element_by_id('su').click() #点击百度一下
        self.wd.find_element_by_link_text('蜗牛学院-移动互联网人才孵化基地_自动化测试培训_JAVA开发培训_...').click()
        time.sleep(2)
        handle=self.wd.current_window_handle #当前焦点所在页面handle
        handles=self.wd.window_handles#打开目标网站后，所有页面handle,返回的是列表
        for i in handles:
            if i!=handle:
                self.wd.switch_to.window(i)
        self.wd.switch_to.frame(self.wd.find_element_by_link_text('在线课堂'))
        time.sleep(2)
        self.wd.find_element_by_link_text('在线课堂').click()
        self.wd.quit() #关闭网页
selenium().count()
# class selenium_login:
#     def __init__(self):
#         self.ws=webdriver.Firefox() #获取Firefox页面
#         self.ws.maximize_window() #让网页全屏  窗口设置
#         self.ws.get('http://localhost/Agileone/')#输入网址
#         self.login()
#         self.sub()
    # def login(self):
    #     time.sleep(2)#等待2秒进入下一个操作
    #     ws=self.ws
    #     ws.find_element_by_id('username').clear()
    #     ele=ws.find_element_by_id('username')
    #     ele.send_keys('admin')#获取用户名文本框并输入用户名admin
    #     ws.find_element_by_id('password').clear()
    #     ws.find_element_by_id('password').send_keys('admin')#获取密码文本框并输入密码admin
    #     ws.find_element_by_id('login').click() #点击登录
    # def sub(self):
    #     time.sleep(3)#等待3秒进行下一步操作
    #     ws=self.ws
    #     # Select(self.ws.find_element_by_id('newitem')).select_by_index(1).click()
    #     # self.ws.find_element_by_id('button').click()
    #     ws.find_element_by_link_text('※ 公告管理 ※').click() #找到公共管理并点击进入
    #     time.sleep(1)
    #     ws.find_element_by_id('noticeid').send_keys('01')
    #     ws.find_element_by_id('headline').clear()
    #     ws.find_element_by_id('headline').send_keys('蜗牛学院')
    #     ws.switch_to.frame(self.ws.find_element_by_class_name('ke-iframe'))#切换焦点
    #     lcc=ws.find_element_by_xpath('/html')#获取绝对路径
    #     lcc.send_keys('sdsds')  #在html中添加内容
    #     time.sleep(2)
    #     ws.find_element_by_id('add').click()
    #     ws.find_element_by_id('')
    #     time.sleep(2)
    #     print(ws.find_element_by_id('msg').text)
    # def __del__(self):
    #     self.ws.quit()
# selenium_login()

