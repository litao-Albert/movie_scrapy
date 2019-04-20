from selenium import webdriver
class Setup2:
    def __init__(self):
        self.ws=webdriver.Firefox()
        self.ws.maximize_window()
        self.ws.get('http://172.16.0.145/index.php?con=admin&act=login')
        self.ws.implicitly_wait(30)