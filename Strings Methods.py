#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Strings Methods</h3>

# In[3]:


quote = "to be or not to be"
print(quote.capitalize())
print(quote)    # notice that the original message is unchanged, because strings are immutable
quote = quote.capitalize()
print(quote)
print(len(quote)) # len() is a function and not a string method
print(quote.upper())
print(quote.find("not")) # returns index at first occurence
print(quote.replace("be","me"))


# In[ ]:




