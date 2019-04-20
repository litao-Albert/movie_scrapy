# coding:utf-8

from  appium import webdriver
import time
desird_caps = {
            'platformName':'Android', #平台的名字
            'deviceName':'0123456789ABCDEF',  #通过adb device查看
            'platformVersion':'4.3',
            # apk包名
            'appPackage':'com.meitu.meiyancamera', #通过 aapt dump badging APK路径 获取
            # apk的launcherActivity
            'appActivity':'com.meitu.meiyancamera.MyxjActivity',
            'unicodeKeyboard':True,
            'resetKeyboard':True
        }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desird_caps)
time.sleep(3)
driver.find_element_by_id('com.meitu.meiyancamera:id/a4j').click()
for i in range(5):
    driver.find_element_by_id('com.meitu.meiyancamera:id/uj').click()
    time.sleep(2)
    driver.find_element_by_id('com.meitu.meiyancamera:id/ayq').click()

