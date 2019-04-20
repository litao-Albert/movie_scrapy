#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/18 12:49
# software:PyCharm Community Edition

import re,time
import requests
from bs4 import  BeautifulSoup
url = 'http://www.budejie.com/video/'
def get_page(url,date=None):
    header = {
       'User - Agent' : 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0 .3396.99 Safari / 53'

    }
    html = requests.get(url,headers=header)
    soup = BeautifulSoup(html.text,'html.parser')
    lists = soup.find_all('a',href=re.compile('http://svideo.spriteapp.com/video/2018/(.*?).mp4'))
    # http: // svideo.spriteapp.com / video / 2018 / (.* ?).mp4
    a = 0
    for i in lists:
        a+=1
        url_href =i.get("href")
        # print(url_href)
        req = requests.get(url_href).content
        print(req)
        with open(str(time.time())+".mp4",'wb') as f:
            f.write(req)
def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url,str(one))
        time.sleep(2)
if __name__ == '__main__':
    get_more_pages(1,2)
