from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
class good:
    def get_wd(self,webdriver):
        self.ws=webdriver
    def test_goods(self):
        driver = self.ws
        driver.find_element_by_link_text("商品中心").click()
        driver.find_element_by_link_text("添加").click()
    def selectone(self):
        driver=self.ws
        Select(driver.find_element_by_id("category_id")).select_by_visible_text("服饰")
        Select(driver.find_element_by_id("type_id")).select_by_visible_text("女式衬衫")
        Select(driver.find_element_by_name("brand_id")).select_by_visible_text("苹果")
    def selecttwo(self):
        driver=self.ws
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("苹果") #商品名称
        driver.find_element_by_name("tag_ids").clear()
        driver.find_element_by_name("tag_ids").send_keys("1111222222333333") #商品关键词
        driver.find_element_by_name("goods_no").clear()
        driver.find_element_by_name("goods_no").send_keys('001') #商品编号
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe'))#切换节点
        driver.find_element_by_xpath("/html/body/div[2]/ul/li[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul/li[2]/img").click()
        driver.find_element_by_xpath("/html/body/div[3]/button").click()
        driver.switch_to.default_content() #关闭节点
    def selectthree(self):
        driver=self.ws
        driver.find_element_by_name('pro_no').clear()
        driver.find_element_by_name('pro_no').send_keys('014') #货号
        driver.find_element_by_name('store_nums').clear()
        driver.find_element_by_name('store_nums').send_keys('20') #库存
        driver.find_element_by_name('warning_line').send_keys('2')
        driver.find_element_by_name('weight').send_keys('2') #重量
        driver.find_element_by_name('sell_price').send_keys('5000')#零售价
        driver.find_element_by_name('market_price').send_keys('6000')#市场价
        driver.find_element_by_name('cost_price').send_keys('5000')#成本价
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[2]/input[1]').click()
        driver.quit()




