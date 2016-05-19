#!/usr/bin/env python
#-*- coding:utf-8 -*-

import poplib
from email.mime.text import MIMEText

pop_server = "pop.163.com"
pop_port = 995
username = "xxxx@163.com"
password = "****"

pobj = poplib.POP3_SSL(pop_server)
pobj.set_debuglevel(1)
try:
    pobj.user(username)
    pobj.pass_(password)
except Exception,e:
    print str(e)

#返回(信数,大小)
#status = pobj.stat()

#(状态,邮件ID列表,)
for email_id in pobj.list()[1]:
    print "eamil_id",email_id.split()[0]
content = '\n'.join(pobj.retr(2)[1])
print MIMEText(content)