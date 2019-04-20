#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/17 22:16
# software:PyCharm Community Edition

# from bs4 import  BeautifulSoup
import  re
import requests
from lxml import etree
s = requests.session()
url = 'http://www.xiaohuar.com/hua/'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

result = s.get(url=url,headers=header).text
results = etree.HTML(result)
imgs_list = results.xpath('//*[@id="list_img"]/div/div[1]/div[1]/div[1]/div[1]/a/img')
num=1
for i in imgs_list:
    img_url = i.attrib["src"]
    print(img_url)
    img_url_content = requests.get(img_url).content
    # print(img_url_content)
    filename = str(num) + '.jpg'
    with open(filename,'wb') as f:
        f.write(img_url_content)








