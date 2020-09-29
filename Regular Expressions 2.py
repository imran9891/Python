#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

pattern = re.compile(r"([A-Za-z!?]).([a])")   # . single character
string = "search this inside of this text please! Imran"

a = pattern.search(string)
print(a.group())
print(a.group(1))
print(a.group(2))

b = pattern.findall(string)
print(b)

# **Regex Functions**

# * findall ->	Returns a list containing all matches

# * search  ->	Returns a Match object if there is a match anywhere in the string. If there is more than one match, only the first occurrence of the match will be returned

# * split	  ->    Returns a list where the string has been split at each match

# * sub	  ->  Replaces one or many matches with a string

