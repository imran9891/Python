#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Dictionary</h3>

# In[ ]:


# Creating dictionary & passing values in different formats.
my_dict = {
    'a' : [1,2,3], # list
    'b' : "hello", # string
    'c' : True # bool
    }

# Creating list and passing dictionary into it.
my_list = [
    {
    'a' : [1,2,3],
    'b' : "hello",
    'c' : True
    },
    {
    'a' : [4,5,6],
    'b' : "bye",
    'c' : False
    }]

# Slicing
print(my_dict["a"])
print(my_dict["a"][1])
print(my_list[1]["a"][2])

