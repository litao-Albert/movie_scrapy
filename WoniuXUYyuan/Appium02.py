import  time
from  appium  import  webdriver
desird_caps={} #APP的基本设置
desird_caps['device']='Android'#设备的系统
desird_caps['platformName']='Android'#设备平台的名字
desird_caps['deviceName']='127.0.0.1:62001'#浏览器的名称
desird_caps['version']='4.3' #系统的版本号
desird_caps['appPackage']='com.miui.calculator'#对应的包名
desird_caps['appActivity']='com.miui.calculator.cal.CalculatorActivity' #对应activity的名称
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desird_caps)
driver.implicitly_wait(30)
driver.find_element_by_name('4').click()
driver.find_element_by_id('com.miui.calculator:id/btn_mul').click()
driver.find_element_by_name('5').click()
# try:
#     driver.find_element_by_name('确定').click()
# except:
#     driver.find_element_by_xpath('//android.widget.ImageView[@content-desc=\'等于\']').click()
driver.tap([(630,1200),(630,1209)],50)
driver.tap([(630,1209),(630,1209)],50)
# size=driver.get_window_size()
# print(size)
# x=size['width']
# y=size['height']
# driver.swipe(x/2,y/2,x/2+350,y/2,1000)
