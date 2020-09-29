#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Docstrings</h3>

# In[ ]:


def test(a):
    """
    info: This is test function which print the argument passed
    """
    print(a)
    
help(test)
print(test.__doc__)

# or we can just type the function name, and automatically a window will pop up with the info 
# about the function.

