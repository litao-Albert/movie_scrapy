#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/25 19:30
# software:PyCharm Community Edition
from bs4 import BeautifulSoup,element
import re
text = '''
<head>
    <meta = charset='UTF-8' >
    <title id =1 href = 'http://example.com/elsie' class = 'title'>
     <!--Test-->
    </title>
</head>
<body>
   <div id= 'ok'>
       <div class = 'nice'>
           <p class = 'p'>
               Hello World
           </p>
           <p class = 'e'>
               风一般得男子
           </p>

       </div>
   </div>
</body> 
</html>
'''
result = BeautifulSoup(text,'html.parser')

#print(result.prettify())
#print(result)
# print(type(result.prettify()))
# print(result.title.name)
# print(result.title.attrs)
# print(result.title.text)
# html = result.find_all('div',class_ = 'nice')
# print(html)
# print("+"*20)
# for i in html:
#     print(i.text)
#     print(i.attrs)
# print(result.find_all(attrs = {'class':'e'}))

# print(result.select('#ok'))
print('--------------------------------------------------')
html1 = result.find_all(id=1)
print(html1)
if type(result.title.string) == element.Comment:
   print(result.title.string)