#coding:utf-8
import smtplib  # 用来登陆smtp服务器
from email.mime.text import MIMEText  # 构建邮件

 #from Excl .TEXT import Excl


def sendMail(content):   # 定义邮件内容
    sender='764114271@qq.com' # 发送人
    password='kgkdewfywfyybceb'


    recv='764114271@qq.com'

    title='TAO s test'


    message=MIMEText(content,'plain','utf-8')
    message['Subject']=title
    message['To']=recv
    message['From']=sender

    print('-'*10)

    server=smtplib.SMTP_SSL('smtp.qq.com',465)  # 登陆腾讯SMTP服务器
    server.login(sender,password) # 登陆自己的stmp账号
    server.sendmail(sender,[recv],message.as_string())   # 接收人需要是列表
    server.quit()
    print('2'*20)

if __name__=="__main__":
 sendMail('HELLO WORLD')