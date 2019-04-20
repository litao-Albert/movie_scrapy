from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import  pyquery as pq
import json
driver = webdriver.Chrome(executable_path="E:\\Download\\chromedriver.exe")
wait =WebDriverWait(driver, 10)
def search():
    try:
        driver.get("https://www.taobao.com/")
        inputs = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        inputs.clear()
        inputs.send_keys("美食")
        submit.click()
        total = wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total"))
        get_product()
        return  total.text

    except TimeoutError:
        search()
def next_page(page_number):
    try:
        inputs = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        inputs.clear()
        inputs.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number))
        get_product()
    except TimeoutError:
        next_page(page_number)
def get_product():
    wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR,"#mainsrp-itemlist.items.item"))
    html = driver.page_source   #得到页面所有的资源
    doc = pq(html)
    items = doc('#mainsrp-itemlist.items.item').items()  #得到所有选择的内容
    for item in items:
        product = {
            'image':item.find('.pic.img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()

        }
        save_file(product)
def save_file(content):
    with open("taobao.txt",'a',encoding='utf-8') as  f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
def mian():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1)) #得到总的页数
    for page in range(2,total+1):
        next_page(page)
if __name__ == '__main__':
    mian()
