#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.message import EmailMessage
from email import encoders

msg = MIMEMultipart()             # Multipurpose Internet Mail Extensions (MIME)

from_add = "i******91@gmail.com"
to_add = "i********3@gmail.com"

msg['From'] = from_add
msg['To'] = to_add
msg['Subject'] = "Personal Message"

body = "Please find the attached file below"
msg.attach(MIMEText(body,'plain'))
filename = './Email/ICC-Rankings.csv'
attachment = open(filename,'r')

part =MIMEBase('application','octet-stream')  #('image','format')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-disposition','attachment; filename = %s' % 'ICC-Rankings.csv')

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(from_add,'**********')

text = msg.as_string()

server.sendmail(from_add,to_add,text)
server.quit()
print('done')

