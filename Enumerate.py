#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Enumerate</h3>

# In[ ]:


# we can pass any iterable to enumerate, and it will store them as separate tuple (index,item)
# with index starting from 0.

for i in enumerate('Hello World'): # str
    print(i)
    
for i,j in enumerate([1,2,3,4]): # list
    print(i,j)

for i in enumerate((1,2,3,4,5)): # tuple
    print(i)

print(list(item for item in enumerate('123456789')))
print((i * i for i in range(8))) # generator object
print([i * i for i in range(8)]) # List comprehension

print(list(enumerate('123456789')))

print(dict(list(enumerate((i * i for i in range(1,11)),1)))) # 1 is starting position

