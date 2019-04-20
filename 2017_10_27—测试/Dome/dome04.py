import http.client #导入http.client包
'''
1.跟主机建立连接
2.构建头部（非必须）
3.构建正文（get不需要）
4.发送请求
5.获取响应
'''
#发送get请求
conn=http.client.HTTPConnection('localhost')#建立与服务器的连接
conn.request('GET','/smeoa/index')
setcookie=conn.getresponse().getheader('set-Cookie')
sessionid=setcookie.split(';')[0] #按；分隔并取出第一部分内容
# content=conn.getresponse().read() #获取页面的响应内容
# print(content.decode()) #将响应的内容按原格式输出
#发送POST请求
conn = http.client.HTTPConnection('localhost') #建议与服务器的连接
data = 'emp_no=admin&password=admin' #构建请求正文
header = { 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Cookie':sessionid}
#发送post请求
conn.request('POST','http://localhost/smeoa/index.php?m=login&a=check_login', body=data, headers=header)
content = conn.getresponse().read() #获取响应
print(content.decode())
if ''== content.decode():
    print('登录成功')
else:
    print('登录失败')
#新增功能
#构建正文
date1='id=&opmode=add&admin=%E5%91%98%E5%B7%A55001%2F%E4%B8%BB%E71%3B&write=%E5%91%98%E5%B7%A55001%2F%E4%B8%BB%E7%AE%A1%7C5001%3B&read=%E5%91%98%E5%B7%A55001%2F%E4%B8%BB%E7%AE%A1%7C5001%3B&folder_list=0&name=test1&folder_name=%E6%A0%B9%E8%8A%82%E7%82%B9&pid=0&sort=02&is_del=0&remark='
#构建头部
header1={ 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8','cookie':sessionid}
conn.request('POST','http://localhost/smeoa/index.php?m=notice_folder&a=save',headers=header1,body=date1.encode())
content1=conn.getresponse().read() #获取页面的响应内容
print(content1.decode())
# 删除功能
date3='id=117&ajax=1'
header3={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
conn.request('POST','http://localhost/smeoa/index.php?m=notice_folder&a=read',headers=header3,body=date3)
content3=conn.getresponse().read()

date2='id=117&opmode=edit&admin=%E5%91%98%E5%B7%A55001%2F%E4%B8%BB&write=%E5%91%98%E5%B7%A55001%2F%E4%B8%BB%E7%AE%A1%7C5001%3B&read=%E5%91%98%E5%B7%A55001%2F%E4%B8%BB%E7%AE%A1%7C5001%3B&folder_list=0&name=%E8%9C%97%E7%89%9B%E5%AD%A6%E9%99%A2&folder_name=%E6%A0%B9%E8%8A%82%E7%82%B9&pid=0&sort=02&is_del=0&remark=&ajax=1'
header2={'Accept': 'application/json, text/javascript, */*; q=0.01',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','cookie':sessionid}
conn.request('POST','http://localhost/smeoa/index.php?m=notice_folder&a=del',headers=header2,body=date2.encode())
content2=conn.getresponse().read() #获取页面的响应内容
print(content2.decode())