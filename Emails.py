#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib

content="Sending mail via Python"

#creates SMTP session
mail=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security  (Transport Layer Security)
mail.starttls()

#Authentication
mail.login('im*****bal9891@gmail.com','*******')

#Sending the mail
mail.sendmail('imr******9891@gmail,com','im*****@gmail.com',content)

#Terminating the session
mail.close()

