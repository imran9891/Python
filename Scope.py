#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Scope</h3>

# In[ ]:


a = 1   # Global variable

def parent_func():
    a = 10
    total = 0
    def local_func():
        return a
        return total  # here it will check what is the value of total, locally, then parent, 
                    # then globally and finally in the built in function.
    return local_func()

print(parent_func())
print(a)

# print(total)    # this will produce an error, as 'total' is undefined globally

# scope of a function remains inside the function only.

#1 - start with local
#2 - parent local
#3 - global
#4 - built in python functions

