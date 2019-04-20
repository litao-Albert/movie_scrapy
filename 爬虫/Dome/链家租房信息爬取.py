#coding:utf-8
import requests
from urllib import request
from lxml import etree
#定义请求的url和请求的头部
s = requests.session()
url = 'https://sz.lianjia.com/zufang/'   # url

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
#    头部
}
# 定义请求
# Request = request.Request(url = url,headers = header)
Request = s.post(url = url,headers = header)
# 发送请求
# response = request.urlopen(Request)
# 收到结果
# result = response.read().decode()
result = Request.text
# 进行数据过滤
# 构建匹配结构
html = etree.HTML(result)   # 把网页源码加载成tree对象，提取里面的信息
# aaa = etree.tostring(html,encoding = 'utf-8')
# print(aaa.decode())
house_list = html.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/p[1]/a')  # 匹配标题
for i in house_list:
    print(i)

house_list1 = html.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]')   # 匹配标题的上一级
l = house_list[0].attrib["title"]
print(l)
# 匹配地址
# address_list = html.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]/div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a')
# for  house in house_list1:
#     house_name =  house.xpath("h2/a")[0].attrib["title"]
#     print(house_name)
#     # 利用 house_list1  去匹配下面相应的地址
#     house_address = house.xpath('div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a')[0].text
#     # title = house.attrib["title"]
#     print('+'*50)
#     print('%s:%s'%(house_name,house_address))
# for address in address_list:
#     print(address.text)
# 把地址和标题对应起来  拼接起来
# 获取第一个标题
