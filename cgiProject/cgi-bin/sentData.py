#coding:utf-8

import random
import datetime
import json

# 生成随机数
date = random.randint(1,9)
# 生成当前时间
now = datetime.datetime.now()
# 设置时间格式
now1 = now.strftime("%H:%M:%S")
# 汇总数据
data_dice = {
    "data":date,
    "time":now1
}
#封装数据
sendData = json.dumps(data_dice)
#返回数据
#cgi 用print作为返回
#返回数据头部
print("Content-type:application/json")
#返回头部结束符
print("\n")
#返回内容
print(sendData)