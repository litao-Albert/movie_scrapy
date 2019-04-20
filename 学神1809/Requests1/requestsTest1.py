#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/19 22:37
# software:PyCharm Community Edition

import requests

session = requests.session()

session_url = 'https://passport.5i5j.com/passport/login?service=https%3A%2F%2Fhz.5i5j.com%2Freglogin%2Findex%3FpreUrl%3Dhttps%253A%252F%252Fhz.5i5j.com%252F%253Flogin%253D1&status=1&city=hz'
session_header = {
       'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
login_cook = session.get(url=session_url,headers=session_header)

login_url = 'https://passport.5i5j.com/passport/sigin?city=hz'

login_header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
login_date = {
    'username':'18225402968',
    'password':'litao201403',
    'aim':'pc',
    'service':'https://hz.5i5j.com/reglogin/index?preUrl=https%3A%2F%2Fhz.5i5j.com%2F',
    'status':1
}
login_content = session.post(url=login_url,headers=login_header,data=login_date)

print(login_content.content.decode())

