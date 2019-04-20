from selenium import webdriver
class Setup:
     def __init__(self):
        self.ws=webdriver.Firefox() #获取网页
        self.ws.maximize_window() #得到全屏
        self.ws.get('http://localhost/smeoa/index.php?m=login&a=index') #输入网址
        self.ws.implicitly_wait(30)

