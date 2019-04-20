#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/25 10:10
# software:PyCharm Community Edition
from  lxml import etree
text = '''
<head>
    <meta = charset='UTF-8' >
    <title id =1 href = 'http://example.com/elsie' class = 'title'>Test</title>
</head>
<body>
   <div class = 'ok'>
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

html = etree.HTML(text)
# result = etree.tostring(html,encoding='utf-8')
# print(result.decode())
# print(type(html))
# print(type(result))
# result = html.xpath("/html/body/div/div/p")
result = html.xpath("//p[@class = 'p']|//p[@class = 'e']")
for i in result:
    print(i.text)
    print(i.tag)
    print(i.attrib)