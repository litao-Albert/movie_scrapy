import requests
from lxml import etree

url = 'https://www.baidu.com/'

response = requests.get(url=url)

response.encoding = 'utf-8'
# print(response.text)

# 把网页源码加载成tree对象，提取里面的信息
tree = etree.HTML(response.text)


result = tree.xpath('//input[@id="su"]/@value')
print(result)
