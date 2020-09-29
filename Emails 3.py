#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Sending mail to multiple users
import smtplib
li=['imr******@gmail.com','*******2@gmail.com']
for id in li:
             s=smtplib.SMTP('smtp.gmail.com',587)
             s.starttls()
             s.login('i*********1@gmail.com','**********')
             msg="Checking the mails by sending it with Jupyter"
             s.sendmail('im*********@gmail.com',id,msg)
             s.close()
            
## From Email Module Directly
import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = '**********891@gmail.com'
email['to'] = 'im********3@gmail.com'
email['subject'] = 'You have won 1000000 $'
email.set_content('Hiiiiiiiiiii')
with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.ehlo()
    server.starttls()
    server.login('im&***8***@gmail.com','***********')
    server.send_message(email)
    print('all good')

