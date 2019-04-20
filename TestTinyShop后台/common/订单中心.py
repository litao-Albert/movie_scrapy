from  selenium import  webdriver
class sale:
    def get_wd(self,webdriver):
        self.ws=webdriver
    def test_sale(self):
        ws=self.ws
        ws.find_element_by_link_text('订单中心').click()
