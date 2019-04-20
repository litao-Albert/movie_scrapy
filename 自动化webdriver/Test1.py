#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/24 10:37
# software:PyCharm Community Edition

from  selenium import webdriver

wd = webdriver.Chrome(executable_path="E:\\Download\\chromedriver.exe")
url = "https://www.baidu.com/"
wd.get(url)
