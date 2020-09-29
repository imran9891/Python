#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create an @authenticated decorator that only allows the function to run if user1 has valid set
# to True

user1 = {
    'name': 'imran',
    'valid': True
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:         
            fn(*args, **kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

