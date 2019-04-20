import time
from appium import webdriver
desird_caps={} #APP的基本设置
desird_caps['device']='Android'#设备的系统
desird_caps['platformName']='Android'#设备平台的名字
desird_caps['deviceName']='127.0.0.1:62001'#浏览器的名称'
desird_caps['version']='4.3' #系统的版本号
desird_caps['appPackage']='com.tencent.mm'#对应的包名
desird_caps['appActivity']='com.tencent.mm.ui.LauncherUI' #对应activity的名称
# desird_caps['chromeOptions']={'androidProcess':'con.tencent.mm:tools'}
# desird_caps['sessionOverride']=True
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desird_caps)
driver.implicitly_wait(120)
driver.find_element_by_id('com.tencent.mm:id/hb').send_keys('litao201403')
driver.find_element_by_name('登录').click()
driver.find_element_by_id('com.tencent.mm:id/ajz').click()
driver.find_element_by_name('微医健康').click()
driver.find_element_by_class_name('就医服务').click()
driver.find_element_by_name('预约挂号').click()

time.sleep(10)
cons=driver.contexts #获取上下文列表
print(cons)