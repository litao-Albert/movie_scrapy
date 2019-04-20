#coding:utf-8
import  time
from  appium import  webdriver

des_caps = {
    'platformName':'Android',
    'deviceNmae':'',
    'platformVesion':'',
    'appPackage':'',
    'appActivity':''
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)
time.sleep(2)  # 休眠2s
