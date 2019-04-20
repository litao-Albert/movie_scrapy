import smtplib
def senderMail(connect):
    host = 'smtp.qq.com'
    port = 465
    sender = '764114271@qq.com'
    recv = ['1549378418@qq.com','764114271@qq.com']
    pwd = 'zbabjzzitmrwbdhd'
    title = '这是一个测试'

    smtp = smtplib.SMTP_SSL(host,port) # 登陆服务器
    smtp.login(sender,pwd) # 登陆自己的账号
    for i in recv:
        msg = 'From:%s\r\n'%sender+\
              'To:%s\r\n'%recv+\
              'Subject:%s\r\n' % title+\
              '\r\n' + \
              connect

    smtp.sendmail(sender,i,msg.encode('utf-8'))

if __name__=="__main__":
 senderMail('ddsdsdsdsdsdsdsddsd')