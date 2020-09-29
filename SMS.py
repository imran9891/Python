#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from twilio.rest import Client
account_sid = 'AC9a017b5d093bff40'
auth_token = 'dfc791496fd7'
Client = Client(account_sid, auth_token)
message = Client.messages.create(from_='+1*****354',
                                 body='hiiiiiiiiii',
                                 to='+91******1')
print(message.sid)

