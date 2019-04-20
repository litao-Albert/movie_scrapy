#coding：utf-8
from 学神1809.zabbix.setting import HOST,password,SENDER,RECV,PORT
import sys
import datetime
import smtplib
from email.mime.text import MIMEText

def writerLog(subject,leven,content):
    now = datetime.datetime.now() #获取当前的时间
    line = "%s[%s]%s;\n"%(now,leven,content)
    message = MIMEText(line,'plain','utf-8')
    message['Subject'] = subject
    message['To'] = RECV
    message['From'] = SENDER
    try:
        smtp = smtplib.SMTP_SSL(HOST,PORT)
        smtp.login(SENDER,password)
        smtp.sendmail(SENDER,[RECV],message.as_string())
        smtp.close()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    subject = "litao test"
    leven = "debug"
    content = "error message"
    writerLog(subject,leven,content)
