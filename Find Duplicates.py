#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Find Duplicates
# Using User-defined Function
some_list = ['a','b','c','b','d','m','n','n']
def duplicates(li):
    d_list = []
    for item in some_list:
        if li.count(item)>1:
            if item not in d_list:
                d_list.append(item)
    return d_list
print(duplicates(some_list))

# Using List Comprehension
some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set(x for x in some_list if some_list.count(x) > 1))
print(duplicates)

