import requests
import json
# r=requests.get('http://localhost/Agileone')
# # print(type(r))
# r.encoding='utf-8'
# print(r.text)#响应的内容
# print(r.encoding) 响应的编码
# print(r.status_code)#响应码
# print(r.cookies)
'''
小微企业的登录
'''
# url='http://localhost/smeoa/index.php?m=login&a=check_login'
# dates={'emp_no':'admin','password':'admin'} #构建正文
# headers={'Content-Type':'application/x-www-form-urlencoded'}
# r=requests.post(url,data=dates) #最基本的POST请求
# print(r.status_code)#响应码
# r.encoding='utf-8' #转码成utf-8
# print(r.cookies)
# print(r.encoding)
# print(type(r))
'''
新增公告
'''
#登录
s=requests.session()
url_login='http://localhost/smeoa/index.php?m=login&a=check_login'
dates={'emp_no':'admin','password':'admin'} #构建正文
header={'Content-Type':'application/x-www-form-urlencoded'}
s.post(url_login,data=dates,headers=header)
# #新增
# url_add='http://localhost/smeoa/index.php?m=notice_folder&a=save'
# header1={'Content-Type':'application/x-www-form-urlencoded'}
# dates1={'id':'', 'opmode':'add', 'admin':'', 'write':'', 'read':'', 'folder_list':'0', 'name':'text7', 'folder_name':'%E6%A0%B9%E8%8A%82%E7%82%B9', 'pid':'0', 'sort':'', 'is_del':'0', 'remark':''}
# # dates1='id=&opmode=add&admin=&write=&read=&folder_list=0&name=text6&folder_name=%E6%A0%B9%E8%8A%82%E7%82%B9&pid=0&sort=&is_del=0&remark='
# s.post(url_add,data=dates1)
# #删除
# url_red='http://localhost/smeoa/index.php?m=notice_folder&a=read'
# header2={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
# dates2={'id=':'108','ajax':'1'}
# s.post(url_red,dates2)
#
# url_del='http://localhost/smeoa/index.php?m=notice_folder&a=del'
# dates3={'id':'108', 'opmode':'edit', 'admin':'', 'write':'', 'read':'', 'folder_list':'0', 'name':'text3', 'folder_name':'%E6%A0%B9%E8%8A%82%E7%82%B9', 'pid':'0', 'sort':'', 'is_del':'0', 'remark':'', 'ajax':'1'}
# header3={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
# s.post(url_del,dates3)
'''
把表单数据序列化
'''
# url='http://httpbin.org/post'
# payload={'some':'data'}
# r=requests.post(url,data=json.dumps(payload))
# print(r.text)
'''
上传文件
'''
# url='http://httpbin.org/post'
# files={'file':open(r'C:\Users\Administrator\Desktop\\a.txt','rb')}
# r=requests.post(url,data=files)
# print(r.text)
'''
验证证书
'''
'''
查询发布会接口
'''
# url='http://127.0.0.1:8000/api/get_event_list/'
# r=requests.get(url,params={'eid':'1'})
# result=r.json()
# print(result)
