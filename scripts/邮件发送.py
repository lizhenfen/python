#!/usr/bin/env python
#-*- coding:utf8 -*-

import smtplib
from email.mime.text import MIMEText
smtp_server =  "smtp.163.com"
smtp_port   = 465
username = "xxx@163.com"
password = "***"
from_addr = 'xxxx@163.com'
to_addr = 'xxxx@qq.com'
msg = MIMEText("你好",_charset='utf8')
msg['Subject']= '好'


smtpobj = smtplib.SMTP_SSL()
smtpobj.connect(smtp_server,smtp_port)
smtpobj.login(username,password)
print smtpobj
smtpobj.sendmail(from_addr,to_addr,msg.as_string())
smtpobj.close()