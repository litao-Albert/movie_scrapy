#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/18 14:35
# software:PyCharm Community Edition

from bs4 import BeautifulSoup
import requests

html = requests.get('https://tieba.baidu.com/p/5950745302')
soup = BeautifulSoup(html.text,'html.parser')
soup_imgs = soup.find_all('img',class_='BDE_Image')
i = 1
for soup_img in soup_imgs:
    img_url = soup_img["src"]
    get_img_content = requests.get(img_url).content
    filename = str(i)+".jpg"
    with open(filename,'wb') as f:
        f.write(get_img_content)
        i+=1
