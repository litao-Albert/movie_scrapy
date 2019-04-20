import time
from selenium.webdriver.support.select import Select
from  Testssmeoa.common.login import Setup
from  Testssmeoa.common import  login
class notice:
    def get_wd(self,webdriver):
        self.ws = webdriver
    def notice(self,name):
        ws=self.ws
        ws.find_element_by_link_text('公告').click()
        ws.find_element_by_link_text('公告管理').click() #点击公告管理
        ws.find_element_by_id('name').clear() #清空名称里面的内容
        ws.find_element_by_id('name').send_keys(name) #输入内容蜗牛学院
        ele=ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/form/div[2]/div/div/span/button')
        ele.click() #点击选择
        #ws.switch_to.frame(ws.find_element_by_class_name('popup_tree_menu panel-body'))
        ws.switch_to.frame(ws.find_element_by_class_name('myFrame'))#切换节点
        # time.sleep(1)
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/ul/li/a/span').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/div[1]/a').click() #点击确定
        # time.sleep(1)
        ws.switch_to.default_content() #关闭节点
        # time.sleep(1)
        ls=ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/form/div[3]/div/div/a/i')
        ls.click() #进入管理
        ws.switch_to.frame(ws.find_element_by_class_name('myFrame')) #获取管理的节点
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/ul/li[4]/a/span').click()
        ws.switch_to.default_content() #关闭节点
        time.sleep(1)
        ws.switch_to.frame(ws.find_element_by_class_name('myFrame')) #获取节点

        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div/nobr[1]/label/span').click()
        time.sleep(2)
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div[2]/label/a/i').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div[4]/label/a').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div[6]/label/a').click()
        ws.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
        ws.switch_to.default_content()
        ws.find_element_by_id('sort').send_keys('01') #操作排序并写入01
        Select(ws.find_element_by_id('is_del')).select_by_index(1) #状态一栏
        #获取备注的路径
        # ws.switch_to.frame(ws.find_element_by_class_name('col-sm-9'))
        lg=ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/form/div[8]/div/textarea')
        lg.send_keys('欢迎来到蜗牛学院第27期测试学习') #在备注中写入内容
        time.sleep(1)
        #点击新增
        ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/a[1]').click()
        try:
            ele=ws.find_element_by_xpath('/div/div[2]/div[2]/h5').text
            if '请输入名称'==ele:
                print('登录失败')
        except:
          print('登录成功')
    def __del__(self):
        self.ws.quit()

