from  selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import  time
wd=webdriver.Firefox()
wd.get('http://www.runoob.com/jqueryui/jqueryui-tutorial.html')
fiset=wd.find_element_by_id('draggable') #获取页面第一个能拖拽的元素
f2=wd.find_element_by_id('draggable2') #获取页面第二个能拖拽的元素
f3=wd.find_element_by_id('draggable3')#获取页面第三个能拖拽的元素
action_chains=ActionChains(wd) #将webdriver作为参数传入，然后实例进行用户操作
action_chains.drag_and_drop(fiset,f2).perform() #将第一个元素拖拽到第二个元素的位置
for i in range(5):
    action_chains.drag_and_drop_by_offset(f3,10,10).perform() #将页面元素第三拖到10个向上，一共拖到5次
    time(2)