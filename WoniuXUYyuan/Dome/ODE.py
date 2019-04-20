from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  logging,traceback
logging.info('sdsasdsdsadsdsdd')
wd=webdriver.Firefox()
wd.get('http://www.baidu.com')
try:
    result=wd.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\sdsda') #截屏并放在左面
    print(result)
except IOError as e:
    print(e)
ele=wd.find_element_by_id('kw')
ele.send_keys(Keys.F12) #实力发送一个F12建
print(ele.get_attribute('name')) #获取搜索筐页面元素的name属性值
ele1=ele.send_keys('蜗牛')
# ele1.send_keys(Keys.RETURN)  #实力发送一个回车建
print(ele.get_attribute('value'))#获取输入狂的文本内容
po=wd.get_window_position() #获取当前窗口的位置
# po=wd.get_window_position(x=200,y=400)  #设置浏览器的位置
print(po['x'])
print(po['y'])
title=wd.title#获取页面title属性值
print(title)
# pageSource=wd.page_source #获取页面HTML的源代码
# print(pageSource)
url=wd.current_url #获取当前url
print(url)
now_handle=wd.current_window_handle #获取当前窗口的句柄
print(now_handle)
logging.info('dasdasdsadssddds')