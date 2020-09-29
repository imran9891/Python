#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_add = 'i**********91@gmail.com'
to_add = '********i@gmail.com'
msg = MIMEMultipart()
msg['From'] = from_add
msg['To'] = to_add
msg['Subject'] = "You have won 1,00,000,000 $"

body = "Please find the attached document below:"
msg.attach(MIMEText(body,'plain'))

filename = "./Email/BKT.jpeg"
attachment = open(filename,"rb")

part = MIMEBase('image', 'jpeg') #('application','octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename=%s' % 'BKT.jpeg')

msg.attach(part)
with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.ehlo()
    server.starttls()
    server.login(from_add,'*************')
    text = msg.as_string()
    server.sendmail(from_add,to_add,text)
    server.quit()
print('done')

