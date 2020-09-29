#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# [param for param in iterable]
print([item for item in range(1,101)])
print([x**2 for x in [1,2,3,4]])
print([char for char in 'hello'])
print([num**2 for num in range(1,101)])
print([num**2 for num in range(1, 101) if num % 2 !=0])

