#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from twilio.rest import Client 
 
account_sid = 'AC6319546a3f976092dc' 
auth_token = '0bbdeba6c52a8e0982b' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14*****86',  
                              body='hiiiiiiiiii',      
                              to='whatsapp:+91*******736' 
                          ) 
 
print(message.sid)

