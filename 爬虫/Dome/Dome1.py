import requests
import json

# POST请求的地址
# post_url = "http://fanyi.baidu.com/translate?aldtype=16047&query=baby&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/baby"
#
# #p配置参数
#
# date={
#     'kw':'baby'
# }
# # 相当于模拟浏览器访问了post_url这个网址
#
# response = requests.post(url=post_url,data=date)
#
# # 声明网站的编码集
# response.encoding='utf-8'
#
# # print(response.text)
# str1 = response.text
# 用json 进行转码
# print(str1)
# json_obj = json.loads(str1,encoding='utf-8')
#
# str2 = json.dumps(json_obj,ensure_ascii=False)
#
# # 写入本地文件
# with open('litao.json','w',encoding='utf-8') as fp:
#     fp.write(str2)
# with open('li.json','r',encoding='utf-8') as f :
#     date = f.read()
#     print(date)
    # json = json.loads(date)
    # print(json)
import hashlib

md5 = hashlib.md5()
md5.update('flask'.encode())
md5.update('111'.encode())
print(md5.hexdigest())