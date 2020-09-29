#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Built-in Module
import random
# print(random)
# help(random)
# dir(random)
print(random.random())
print(random.randint(2,50))
print(random.choice([1,2,3,4,5]))
li = [1,2,3,4,5]
random.shuffle(li)
print(li)

