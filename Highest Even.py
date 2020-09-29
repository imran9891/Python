#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Highest Even</h3>

# In[ ]:


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)
print(highest_even([10,2,3,14,88,11]))

