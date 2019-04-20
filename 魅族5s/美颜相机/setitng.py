#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/10 19:19
# software:PyCharm Community Edition

from appium import  webdriver
import time

des_caps = {
    'platformName':'Android',
    'deviceName':'612QKBAR269Z8',
    'platformVersion':'4.3',
    'appPackage':'com.android.settings',
     'appActivity':'com.android.settings.Settings$AccessibilitySettingsActivity',
     # com.android.settings.Settings$AccessibilitySettingsActivity
    'unicodeKeyboard':True,
    'resetKeyboard':True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)
time.sleep(3)
driver.find_element_by_id('com.meizu.flyme.launcher:id/app_name').click()
time.sleep(1)
# driver.find_element_by_id('com.android.settings:id/title').click()
driver.find_element_by_class_name('android.widget.TextView').click()
driver.find_element_by_link_text('关于手机').click()



