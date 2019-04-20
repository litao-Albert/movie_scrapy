from  selenium import webdriver

class search:
    def get_wd(self,webdriver):
        self.ws=webdriver
    def search(self,se):
        self.ws.find_element_by_id('search-keyword').clear()
        self.ws.find_element_by_id('search-keyword').send_keys(se)
        self.ws.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/form/button').click()
        try:
            self.ele1=self.ws.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/dl/dd/ul/li/dl/dd[2]/span').text
            if '￥3367.00'==self.ele1:
                print('搜索功能可用')
        except:
            print('搜索功能不可用')