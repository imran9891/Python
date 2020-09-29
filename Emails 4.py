#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=Template(Path('./Email/index.html').read_text())
email=EmailMessage()
email['from']= 'Md Imran'
email['to']= 'i********3@gmail.com'
email['subject']= 'You won 1,00,000 dollars!'
email.set_content(html.substitute({'name':'Imran'}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('im*********1@gmail.com','*********')
    smtp.send_message(email)
    print('all good')

