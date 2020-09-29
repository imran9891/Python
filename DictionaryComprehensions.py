#!/usr/bin/env python
# coding: utf-8

# In[ ]:


my_dict = {
    'a': 1,
    'b': 2}
print({k:v**2 for k,v in my_dict.items() if v % 2 == 0})

print({item:item*2 for item in [1,2,3]})

