#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/18 0:05
# software:PyCharm Community Edition

import requests
from lxml import etree
s = requests.session()
import re
url = 'http://www.xiaohuar.com/hua/'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

result = s.get(url=url,headers=header)

content = str(result.content)
# print(content)
res = r'<img (.*?)>'
result_list = re.findall(res,content)
# print(result_list)
for url in  result_list:
    print(url)
