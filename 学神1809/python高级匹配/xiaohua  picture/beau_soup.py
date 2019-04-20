#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/18 10:52
# software:PyCharm Community Edition

from bs4 import BeautifulSoup
import requests

result = requests.get('https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%A0%A1%E8%8A%B1&step_word=&hs=2&pn=0&spn=0&di=169975858140&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=1384152344%2C3670480287&os=1661854179%2C3430463690&simid=0%2C0&adpicid=0&lpn=0&ln=1886&fr=&fmq=1542512058279_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.cqtimes.cn%2FUploads%2FPicture%2F2017-09-12%2F2017091214435121.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3F2jpp57ptw5_z%26e3Bp7xt_z%26e3Bv54_z%26e3BvgAzdH3Fypq-da80al8bAadElRaa_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=').text
soup = BeautifulSoup(result,'html.parser')
uls = soup.find_all('img',class_="currentImg")
num = 2
for url in uls:
    img_url = url["src"]
    print(img_url)
#     get_img_url = requests.get(img_url).content
#     filename = str(num)+'.jpg'
#     with open(filename,'wb') as f:
#         f.write(get_img_url)




