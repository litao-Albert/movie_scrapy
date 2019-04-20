from email.mime.text import MIMEText
import smtplib,time,random
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def Sendmail(content):

    user = "764114271@qq.com"
    pwd = "zbabjzzitmrwbdhd"
    recv = "1549378418@qq.com"
    host = 'smtp.qq.com'

    msg = MIMEMultipart()



    msg['Subject'] = 'This is a Test'
    msg['From'] = user
    msg['To'] = recv

    part = MIMEText(content)

    msg.attach(part)

    part = MIMEApplication(open('D:\\test2\\1.png','rb').read())
    part.add_header('content-disposition', 'attachment', filename='D:\\test2\\1.png')
    with open("D:\a.txt") as f:
        lines = f.readlines()
        name = random.choice(lines)
        names = name.decode().replace('\n','')
        msg =MIMEText(names,'plain','utf-8')



    server = smtplib.SMTP(host,25)
    server.login(user,pwd)
    server.sendmail(user,recv,msg.as_string())
    server.quit()

Sendmail('hello world')

