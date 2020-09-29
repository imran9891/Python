#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Dictionary Method 2</h3>

# In[ ]:


user = {
        "name": "imran",
        "sex": "M",
        "age": 25
        }

# print(user["height"]) # this will give us error, as height key doesn't exit in the dictionary.

print(user.get("height")) # using get function returns None if key passed doesn't exists.

print(user.get("height", 6)) # if the key value pair doesn't exit, then it will write the default value.
print(user)

# new way to create a dictionary
user2 = dict(name = "imran", age = 25)
print(user2)
print(user2["name"])

