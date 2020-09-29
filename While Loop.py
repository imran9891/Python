#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">While Loop</h3>

# In[ ]:


i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("done")
    
while True:
    response = input("say something: ")
    if (response == 'bye'):
        break

