	#coding:utf-8
import paramiko
#实例化ssh客户端
ssh = paramiko.SSHClient()
#创建默认的白名单
policy = paramiko.AutoAddPolicy()
#设置白名单
ssh.set_missing_host_key_policy(policy)
#链接服务器
ssh.connect(
    hostname = "192.168.1.106 ", #服务器的ip
    port = 22, #服务器的端口
    username = "litao", #服务器的用户名
    password = "123456" #用户名对应的密码
)
#远程执行命令
stdin,stdout,stderr = ssh.exec_command("ls")
    #exec_command 返回的对象都是类文件对象
    #stdin 标准输入 用于向远程服务器提交参数，通常用write方法提交
    #stdout 标准输出 服务器执行命令成功，返回的结果  通常用read方法查看
    #stderr 标准错误 服务器执行命令错误返回的错误值  通常也用read方法
#查看结果，注意在Python3 字符串分为了：字符串和字节两种格式，文件返回的是字节
result = stdout.read().decode()

print(result)