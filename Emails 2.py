#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
toaddr='imra******3@gmail.com'
msg="Testing message using Python Scripts"
username='im********1@gmail.com'
password='********'
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(username,toaddr,msg)
server.close()
print("Sent my 1st mail via Python")


## By User Input

##Send email using user input
import smtplib
to=input("Enter mail id: ")
sub=input("Enter the subject: ")
bodymsg=input("Enter the body of the mail: ")
gmail_user='imran*******1@gmail.com'
gmail_pwd='*********'
smtpserver=smtplib.SMTP('smtp.gmail.com',587)
smtpserver.starttls()
smtpserver.login(gmail_user,gmail_pwd)
header='To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'subject: ' + sub + ''
print(header)
msg=header + '\n' +bodymsg + '\n\n'
smtpserver.sendmail(gmail_user,to,msg)
print("Sending Done")
smtpserver.close()

