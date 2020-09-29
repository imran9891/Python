#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

eid = pd.read_excel("./Email/ID.xlsx")
id = eid['Email IDs']

# User_input
from_add = input('Sender Mail Id: ')
subject = input('Give the subject: ')
body = input('Enter your message: ')
password = input('Password please: ')
to_add = []
for dest in id:
    to_add.append(dest)

msg = MIMEMultipart()
msg['From'] = from_add
msg['To'] = to_add
msg['Subject'] = subject
content = body

msg.attach(MIMEText(content,'plain'))

filename = "./Email/empty.txt"
attachment = open(filename,'r')

part = MIMEBase('application','octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename = %s' % 'check.txt')

msg.attach(part)
with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.ehlo()
    server.starttls()
    server.login(from_add,password)
    text = msg
    for emailid in to_add:
        server.sendmail(from_add, emailid, text)
    server.quit()
print('done')

