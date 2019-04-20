import requests
import json

# POST请求的地址
post_url = 'http://fanyi.baidu.com/sug'

# 配置参数
data = {
	'kw':'baby'
}

# 相当于模拟浏览器访问了post_url这个网址
response = requests.post(url=post_url,data=data)

# 声明网站的编码集
response.encode='utf-8'

# print(response.text)
# 保存从网站获取到的数据
str1 = response.text

json_obj = json.loads(str1,encoding='utf-8')
str2 = json.dumps(json_obj,ensure_ascii=False)

# 写入本地文件
with open('l.json','w',encoding='utf-8') as fp:
	fp.write(str2)

# print(content)